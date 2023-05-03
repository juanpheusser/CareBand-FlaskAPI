from datetime import datetime
from influxdb_client import Point
from influxdb_client.client.write_api import ASYNCHRONOUS, SYNCHRONOUS
import os
from influxdb_client import InfluxDBClient




def parseData(data):

    print(data)


    return data



def postToInfluxDB(data):
    url = os.getenv("URL")
    token = os.getenv("INFLUXDB_TOKEN")
    org = os.getenv("ORG")
    bucket = os.getenv("BUCKET")
    client = InfluxDBClient(url=url,
                            token=token,
                            org=org)
        
    write_api = client.write_api(write_options=SYNCHRONOUS)

    try:
        p = Point("SensorData").tag("Prototype", 1) \
            .field("lat", float(data['lat'])) \
            .field("long", float(data["long"])) \
            .field("speed", float(data["speed"])) \
            .field("heading", float(data["heading"])) \
            .field("altitude", float(data["altitude"])) \
            .field("temperature", float(data["temperature"])) \
            .field("battery", float(data["battery"])) \
            .field("acceleration_x", float(data["acceleration_x"])) \
            .field("acceleration_y", float(data["acceleration_y"])) \
            .field("acceleration_z", float(data["acceleration_z"])) \
            .field("rotation_x", float(data["rotation_x"])) \
            .field("rotation_y", float(data["rotation_y"])) \
            .field("rotation_z", float(data["rotation_z"])) \
            .time(datetime.now())
        
    except:
        p = Point("SensorData").tag("Prototype", 1) \
            .field("lat", float(data['lat'])) \
            .field("long", float(data["long"])) \
            .field("speed", float(data["speed"])) \
            .field("heading", float(data["heading"])) \
            .field("altitude", float(data["altitude"])) \
            .field("temperature", float(data["temperature"])) \
            .field("battery", float(data["battery"])) \
            .time(datetime.now())

    
    write_api.write(bucket=bucket, org=org, record=p)

    #write_api.__del__()
    #client.__del__()
