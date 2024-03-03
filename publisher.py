import os
import paho.mqtt.client as mqtt
import time
from random import randrange


broker = 'localhost'
port = 1883
topic = 'test/topic1'
id = f"pub_{randrange(10)}"




def main():
    
    client = mqtt.Client(client_id=id)  
    client.connect(broker, port)

    

    for _ in range(10):
        d = randrange(10)
        client.publish(topic=topic, payload=d)
        print(f"On topic {topic} published message: {d}")
        time.sleep(1)


    client.disconnect()

if __name__ == '__main__':


    
    main()
    






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