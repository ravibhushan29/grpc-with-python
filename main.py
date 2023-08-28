import rides_pb2 as pb
from datetime import datetime

# print(pb.POOL)
# print(pb.RideType.Name(pb.POOL))
# print(pb.RideType.Value('REGULAR'))

loc = pb.Location(lat=32.5270941, lng=34.9404309)
print(loc)

request = pb.StartRequest(car_id=95, driver_id='McQueen', passenger_ids=['p1', 'p2', 'p3'], type=pb.POOL, location=loc)
time = datetime(2023, 2, 13, 14, 39, 42)
request.time.FromDatetime(time)
print(request)
#region ToDatetime
time2 = request.time.ToDatetime()
print(type(time2), time2)
# endregion
from google.protobuf import timestamp_pb2
now = timestamp_pb2.Timestamp()
now.GetCurrentTime()
print(now)
# print(request.location)
#
# print(request.location.lat)

from google.protobuf.json_format import MessageToJson

data = MessageToJson(request)
print(data)
print('json type:', type(data))
print('json size:', len(data))

#region marshal
data = request.SerializeToString()
print('type:', type(data))
print('size:', len(data))

#region unmarshal
# request2 = pb.StartRequest()
# request2.ParseFromString(data)
# print(request2)
