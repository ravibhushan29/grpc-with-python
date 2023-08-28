from collections import namedtuple

import grpc

import rides_pb2_grpc as rpc
import rides_pb2 as pb
import logging
from datetime import datetime, timedelta
from time import sleep

logging.basicConfig(level=logging.INFO)
LocationEvent = namedtuple('LocationEvent', 'car_id time lat lng')

class ClientError(Exception):
    pass


def rand_events(count):
    time = datetime(2023, 2, 13, 14, 39, 42)
    lat, lng = 51.4871871, -0.1266743
    for _ in range(count):
        yield LocationEvent(car_id=7, time=time, lat=lat, lng=lng)
        time += timedelta(seconds=17.3)
        lat += 0.0001
        lng += 0.0001
        sleep(0.1)


class Client:

    def __init__(self, addr):
        self.chan = grpc.insecure_channel(addr)
        self.stub = rpc.RidesStub(self.chan)
        logging.info('connected to %s', addr)

    def close(self):
        self.chan.close()

    def ride_start(self, car_id, driver_id, passenger_ids, type, lat, lng, time):
        request = pb.StartRequest(car_id=car_id, driver_id=driver_id,
                                  passenger_ids=passenger_ids,
                                  type=pb.POOL if type == 'POOL' else pb.REGULAR,
                                  location=pb.Location(lat=lat, lng=lng)
                                  )
        request.time.FromDatetime(time)
        logging.info('ride started to %s', request)
        response = self.stub.Start(request)
        return response.id

    def track(self, event):
        self.stub.Track(track_request(event) for event in events)


def track_request(event):
    request = pb.TrackRequest(car_id=event.car_id, location=pb.Location(lat=event.lat, lng=event.lng))
    request.time.FromDatetime(event.time)
    return request


if __name__ == '__main__':
    import config
    # addr = f'{config.HOST}:{config.PORT}'
    addr = f'[::]:{config.PORT}'
    client = Client(addr)
    events = rand_events(7)

    # loc = pb.Location(lat=32.5270941, lng=34.9404309)
    # time = datetime(2023, 2, 13, 14, 39, 42)
    # res = client.ride_start(car_id=95, driver_id='McQueen', passenger_ids=['p1', 'p2', 'p3'], type=pb.POOL,
    #                         lat=51.4871871, lng=34.9404309, time=time)
    # logging.info(f'output: {res}')
    try:
        client.track(events)
    except ClientError as err:
        raise SystemExit(f'error:{err}')
