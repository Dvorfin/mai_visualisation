import os
import paho.mqtt.client as mqtt
from random import randrange


broker = 'localhost'
port = 1883
topic = 'test/topic1'
id = f"sub_{randrange(10)}"


def on_message(client, userdata, msg):
    print(f"\nOn topic {msg.topic} received message: {str(msg.payload.decode('utf-8'))}") 
  


def on_connect(client, userdata, flags, rc):
    print(f"Connected with res code: {str(rc)}")
    print(f"Subscriber connected to topic: {topic}")
    print('\n')



def main():
    client = mqtt.Client(client_id=id)

    client.connect(broker, port)  # connecting to topic
    client.subscribe(topic)        # subscribing to topic 
    client.on_connect = on_connect  # on connect
    client.on_message = on_message  # on msg

    try:
        print("Press CTRL+C to exit.")
        client.loop_forever()       # looping 
    except Exception as e:
        print(f"Error: {e}")
        print(f"Disconnecting from broker: {broker}")


if __name__ == '__main__':

    main()
    
 