import json
import random
import os


def generate_dict() -> dict:
    x_grad = random.uniform(0.0, 360.0)
    y_grad = random.uniform(0.0, 360.0)
    z_grad = random.uniform(0.0, 360.0)

    x_a = random.uniform(0.0, 10.0)
    y_a = random.uniform(0.0, 10.0)
    z_a = random.uniform(0.0, 10.0)

    json_data = {
                "x_grad": x_grad, 
                "y_grad": y_grad,
                "z_grad": z_grad,
                
                "x_a": x_a,
                "y_a": y_a,
                "z_a": z_a,
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
    generate_json()
    
    
