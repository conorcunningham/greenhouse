def on_message(client, userdata, message):
    print("message client=", client._client_id)
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    print("message userdata=", userdata)


def on_log(client, userdata, level, buf):
    print("log: ", buf)
    print(f"log: {client=} {userdata=}, {level=}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"on subscribe: {client=} {userdata=} {mid=} {granted_qos=}")


def on_publish(client, userdata, mid):
    print(f"on publish:{client=}, {userdata=}, {mid=}")


def on_connect(client, userdata, flags, rc):
    print(f"on connect: server: {str(rc)} {userdata=} {flags=} {client=}")
