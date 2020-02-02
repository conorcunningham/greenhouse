import paho.mqtt.client as mqtt
from src.callbacks import *

USER = "test"
PASS = "testing123"
HOSTNAME = "192.168.2.10"


def main():

    # initalise our mqtt client
    client = mqtt.Client("test_client")

    # attach our custom callback methods
    # these are imported from src/callback.py on line 2 of this file
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish

    # attach a logger
    client.on_log = on_log

    # if your server uses authentication, set them here
    client.username_pw_set(USER, password=PASS)

    # user defined data that is available on callbacks
    client.user_data_set("messages from python test")

    # connect to the mqtt server
    client.connect(HOSTNAME)

    # Let's subscribe to the topic 'test'
    client.subscribe("test")

    # start mqtt client loop
    client.loop_start()

    # let's publish a message of 'hello from python' to topic 'test'
    client.publish("test", "hello from python")

    # stop the loop
    client.loop_stop()

    rc = 0
    while rc == 0:
        rc = client.loop()
    print("rc: " + str(rc))


if __name__ == '__main__':
    main()
