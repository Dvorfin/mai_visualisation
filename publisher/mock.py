import json
import random
import os
import datetime


def emulate_battery():
    current_time = datetime.datetime.now().minute
    current_time = current_time * 1.695

    if current_time >= 100:
        current_time = 100

    return current_time


def generate_dict() -> dict:
    x_grad = random.uniform(0.0, 360.0)
    y_grad = random.uniform(0.0, 360.0)
    z_grad = random.uniform(0.0, 360.0)

    x_a = random.uniform(0.0, 10.0)
    y_a = random.uniform(0.0, 10.0)
    z_a = random.uniform(0.0, 10.0)


    batt = emulate_battery()


    json_data = {
                "x_grad": x_grad, 
                "y_grad": y_grad,
                "z_grad": z_grad,
                
                "x_a": x_a,
                "y_a": y_a,
                "z_a": z_a,

                "batt": batt
                }
    
    return json_data


def generate_json() -> None:

    data = generate_dict()
    json_data = json.dumps(data, indent=2)
    
    print(f"Successfully generated json file")
    return json_data


def main():
    pass



if __name__ == '__main__':
    #generate_json()
    emulate_battery()
    
    
