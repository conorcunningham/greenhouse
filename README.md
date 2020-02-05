# Simple Python MQTT Example

This is a work in progress and there will be many, many breaking changes.

## ESP32
Code for sensing temperature and humidity data, and transmitting that data encoded in JSON over MQTT is found in [temp_humidity_dht22_mqtt.cpp](./src/esp32/temp_humidity_dht22_mqtt.cpp)

## Python MQTT client
Included is a small test client for MQTT written in Python. It currently does the following:

* Retrieves topics and sensors from the Django API
* Listens for MQTT topics as retrieved from the API
* If a topic is retrieved from a sensor that was fecthed from the API, it will then POST the payload of the message to the API

The main program file can be found here: [mqtt-test.py](mqtt-test.py)

## Django API

Use the following URLs (they are relative to http://your-hostname:port/):
* api/sensors : Retrieve and create sensors
* api/topics : Retrieve and create topics
* api/temperatures: Retrieve and create temperature + humidity records
* api/sensor-topics: Retreive and create records of topics and associated sensors
* api/sensor-value: Retrieve and create records for other types of sensors

As an example, if you were developing on your local laptop and using port 8000 for Django, the URL to access sensors would be http://localhost:8000/api/sensors. If the system were in production at https://greenhouse.conorcunningham.net, then the URL to access sensors would be https://greenhouse.conorcunningham.net/api/sensors

## Database setup
I've chosen to use Postgres as my database. I'll list the steps I've used on Ubuntu server 19.10

#### Install Postgres
```bash

```
```
conor@wintermute$ sudo su - postgres
postgres@wintermute$ psql
```

#### Create a db user and grant it privileges
```sql
create role greenhouse_user with login password 'greenhouse';

ALTER ROLE greenhouse_user createdb;

quit
```
Now, login to Postgres as user you just created
```bash
psql -U greenhouse_user -h localhost postgres
```
And create your new db
```sql
create database greenhouse;
```