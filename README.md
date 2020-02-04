# Simple Python MQTT Example

This is a work in progress and there will be many, many breaking changes.

## ESP32
Code for sensing temperature and humidity data, and transmitting that data encoded in JSON over MQTT is found in [temp_humidity_dht22_mqtt.cpp](.src/esp32/temp_humidity_dht22_mqtt.cpp)

## Python MQTT client
Included is a small test client for MQTT written in Python. It currently does the following:

* Retrieves topics and sensors from the Django API
* Listens for MQTT topics as retrieved from the API
* If a topic is retrieved from a sensor that was fecthed from the API, it will then POST the payload of the message to the API

The main program file can be found here: [mqtt-test.py](.src/mqtt-test.py)

## Django API

Use the following URLs (they are relative to http://your-hostname:port/):
* api/sensors : Retrieve and create sensors
* api/topics : Retrieve and create topics
* api/temperatures: Retrieve and create temperature + humidity records
* api/sensor-topics: Retreive and create records of topics and associated sensors
* api/sensor-value: Retrieve and create records for other types of sensors

As an example, if you were developing on your local laptop and using port 8000 for Django, the URL to access sensors would be http://localhost:8000/api/sensors. If the system were in production at https://greenhouse.conorcunningham.net, then the URL to access sensors would be https://greenhouse.conorcunningham.net/api/sensors
