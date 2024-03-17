import paho.mqtt.client as mqtt
import time
from random import randrange
import os
import sys

#sys.path.insert(1, os.path.join(sys.path[0], '..'))     # необходимо для подтягивания пути к моку
from mock import generate_json


broker = 'mosquitto_broker'     # название брокера (его IP) свопадает с название контейнера москито
#broker = 'localhost'
port = 1883     
topic = 'test/topic1'       
id = f"pub_{randrange(10)}"     # id паблишера

json_path = "/home/toor/mai_visualisation/mock/json_data/"



FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


def on_disconnect(client, userdata, rc):
    print(f"\nDisconnected with result code: {rc}")
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        print(f"Reconnecting in {reconnect_delay} seconds...")
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            print("Reconnected successfully!")
            return
        except Exception as err:
            print(f"{err}. Reconnect failed. Retrying...", )

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1

    print(f"Reconnect failed after {reconnect_count} attempts. Exiting...")


def publish(client):
    msg_count = 0
    #json_array = read_json()

    while True:
        time.sleep(1)
        # msg = f"messages: {msg_count}"

        # json_data = json_array[msg_count]  # проходимся по джосн файлам

        # with open(json_path + f"json_{msg_count}.json", 'r') as file:
        #     msg = file.read()  
        msg = generate_json()

        result = client.publish(topic, msg)

        status = result[0]
        if status == 0:
            print(f"\nSend `{msg}` to topic `{topic}`\n")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        #if msg_count >= len(json_array):
        if msg_count >= 1000:
            break



def read_json():
    '''Возвращаем кол-во json файлов для отправки'''
    files = os.listdir(json_path)
    return files


def main():
    
    client = mqtt.Client(client_id=id)  
    client.connect(broker, port)
    client.on_disconnect = on_disconnect

    client.loop_start()
    publish(client)

    # for _ in range(10):
    #     d = randrange(10)
    #     client.publish(topic=topic, payload=d)
    #     print(f"On topic {topic} published message: {d}")
    #     time.sleep(1)


    client.loop_stop()

    client.disconnect()


if __name__ == '__main__':


    main()
    #print(read_json())
    






# def read_data_from_file():
#     #os.chdir('/home/toor/ITS_MAI/task4/')
#     readpath = '/home/toor/mai_visualisation/data.txt'  # path to file 
#     if not os.path.exists(readpath):
#         print('File not found')
#     else:
#         with open(readpath) as f:
#             #contents = f.read()
#             contents = f.readlines()
#             return contents
