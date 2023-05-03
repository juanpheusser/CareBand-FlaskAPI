from datetime import datetime
from influxdb_client import Point
from influxdb_client.client.write_api import ASYNCHRONOUS, SYNCHRONOUS
from dotenv import dotenv_values
from influxdb_client import InfluxDBClient




def parseData(data):

    print(data)


    return data



def postToInfluxDB(data):
    config = dotenv_values(".env")
    client = InfluxDBClient(url=config["URL"],
                            token=config["INFLUXDB_TOKEN"],
                            org=config["ORG"])
    
    print(config["BUCKET"])
    
    write_api = client.write_api(write_options=SYNCHRONOUS)

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
    
    write_api.write(bucket=config["BUCKET"], org=config["ORG"], record=p)

    print("Wrote data to InfluxDB")

    #write_api.__del__()
    #client.__del__()
