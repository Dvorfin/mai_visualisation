import paho.mqtt.client as mqtt
from random import randrange
import time
import json



broker = 'mosquitto_broker'
#broker = 'localhost'
port = 1883
topic = 'test/topic1'
id = f"sub_{randrange(10)}"
msg_count = 0

json_path = "/home/toor/mai_visualisation/subscriber/recieved_json/"


FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


def save_recieved_data(data, count):
    '''Функция для сохранения данных, полученных с брокера'''
    global msg_count
    path = json_path + f"json_{count}.json"
    with open(path, 'w') as file:
        data = json.loads(data)     # десерализуемы данные из строки в словарь
        json.dump(data, file, indent=2)     # сереализуем данные в json



def on_message(client, userdata, msg):
    global msg_count
    print(f"\nOn topic `{msg.topic}` received message: {str(msg.payload.decode('utf-8'))}") 
    #save_recieved_data(msg)
    msg = msg.payload.decode('utf-8')
    msg_count += 1
   
    try:
        save_recieved_data(msg, msg_count)
    except Exception as err:
        print(f"Failed to save data, error: {err}")


def on_connect(client, userdata, flags, rc):
    print(f"Connected with res code: {str(rc)}")
    print(f"Subscriber connected to topic: {topic}")
    print('\n')


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        print("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            print("Reconnected successfully!")
            return
        except Exception as err:
            print("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
        
    print("Reconnect failed after %s attempts. Exiting...", reconnect_count)


def main():
    client = mqtt.Client(client_id=id)

    client.connect(broker, port)  # connecting to topic
    client.subscribe(topic)        # subscribing to topic 
    client.on_connect = on_connect  # on connect
    client.on_message = on_message  # on msg
    client.on_disconnect = on_disconnect

    try:
        print("Press CTRL+C to exit.")
        client.loop_forever()       # looping 
    except Exception as e:
        print(f"Error: {e}")
        print(f"Disconnecting from broker: {broker}")


if __name__ == '__main__':

    main()
    
 