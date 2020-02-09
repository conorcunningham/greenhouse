from collections import deque
from . api import Greenhouse
import json

# initialise our message queue
messages = deque(maxlen=1000)

# auth parameters for django greenhouse
username = 'conor'
password = 'aphextwin21'
host = "https://greenhouse.cunningtek.com/api/"
host = "http://localhost/api/"

# initialize a new greenhouse instance and get a token
greenhouse = Greenhouse(host, username, password)
print(greenhouse.get_token())


# get all topics and sensors from the API
topics_data = greenhouse.fetch_data("topics")
sensors_data = greenhouse.fetch_data("sensors")
print(f"{topics_data=}")
print(f"{sensors_data=}")


# these will hold information about each topic and sensor
topics = {}
sensors = {}

for topic in topics_data:
    topics[topic["name"]] = topic["id"]

for sensor in sensors_data:
    sensors[sensor["name"]] = sensor["id"]


# noinspection PyUnusedLocal
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))
    print(f"{payload=}")

    # print("message client=", client._client_id)
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    print("message userdata=", userdata)
    payload = json.loads(message.payload.decode("utf-8"))
    # message = {
    #     "topic": message.topic,
    #     "payload": str(message.payload.decode("utf-8")),
    #     "timestamp": "put timestamp here"
    # }
    # messages.append(message)

    if message.topic in topics:
        topic_id = topics[message.topic]
        if payload["sensor_name"] in sensors:
            sensor_id = sensors[payload["sensor_name"]]
            data = {
                "sensor": sensor_id,
                "topic": topic_id,
                "temperature": payload["temperature"],
                "humidity": payload["humidity"]
            }
            request = greenhouse.add_temperature_values(data)
            if "error" in request:
                print(request["error"], request["error_code"])


def on_log(client, userdata, level, buf):
    print("log: ", buf)
    print(f"log: {client=} {userdata=}, {level=}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"on subscribe: {client=} {userdata=} {mid=} {granted_qos=}")


def on_publish(client, userdata, mid):
    print(f"on publish:{client=}, {userdata=}, {mid=}")


def on_connect(client, userdata, flags, rc):
    print(f"on connect: server: {str(rc)} {userdata=} {flags=} {client=}")
