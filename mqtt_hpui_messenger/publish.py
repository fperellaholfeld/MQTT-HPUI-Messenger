import paho.mqtt.client as mqtt
import time

def main(ip: str, port: int, protocol: str) -> None:
    """
    ip: IP of the broker.
    port: port of the broker
    protocol:  Leave empty for `tcp` if using websockets, pass `websockets`
    """

    if protocol not in ("websockets", None):
        raise Exception("Only `websockets` allowed for protocol")
    client = mqtt.Client(transport=protocol)
    client.connect(ip, port)

    client.publish("test message for HPUI Messenger with Android", True)


if __name__ == '__main__':
    main("127.0.0.1", 80, "websockets")