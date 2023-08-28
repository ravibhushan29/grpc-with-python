from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from uuid import uuid4
import grpc

import logging

import rides_pb2 as pb
import rides_pb2_grpc as rpc
from grpc_reflection.v1alpha import reflection

import validates

logging.basicConfig(level=logging.INFO)


def new_ride_id():
    return uuid4().hex


def load_credentials():
    with open(config.cert_file, 'rb') as fp:
        cert = fp.read()

    with open(config.key_file, 'rb') as fp:
        key = fp.read()

    return grpc.ssl_server_credentials([(key, cert)])


class Rides(rpc.RidesServicer):
    def Start(self, request, context):
        logging.info('ride: %r', request)
        try:
            validates.start_request(request)
        except validates.Error as err:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f'{err.field}' is {err.reason})
            raise err
        # todo: save ride in database
        ride_id = new_ride_id()
        return pb.StartResponse(id=ride_id)

    def Track(self, request_iterator, context):
        count = 0
        for request in request_iterator:
            # todo: save ride in database
            logging.info('track %s', request)
            count += 1
        return pb.TrackResponse(count=count)


class TimingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        start = perf_counter()
        try:
            return continuation(handler_call_details)
        finally:
            duration = perf_counter() - start
            name = handler_call_details.method
            logging.info('%s took %.3fsec', name, duration)


if __name__ == '__main__':
    import config

    try:
        server = grpc.server(ThreadPoolExecutor(max_workers=10), interceptors=[TimingInterceptor()])
        rpc.add_RidesServicer_to_server(Rides(), server)
        names = (pb.DESCRIPTOR.services_by_name['Rides'].full_name, reflection.SERVICE_NAME)
        reflection.enable_server_reflection(names, server)

        addr = f'[::]:{config.PORT}'

        # server.add_insecure_port(addr)
        credentials = load_credentials()
        server.add_secure_port(addr, credentials)
        server.start()
        logging.info('server ready on %s', addr)
        server.wait_for_termination()
    except Exception as e:
        logging.exception("An error occurred during server startup: %s", str(e))
