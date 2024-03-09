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


def generate_json(num: int = 1) -> None:
    current_directory = os.getcwd()
    print(f"Saving jsons in {current_directory}")

    
    for i in range(num):
        json_file_path = os.path.join(current_directory, f"mock/json_data/json_{i}.json")
        data = generate_dict()

        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=2)
    
    print(f"Successfully generated {num} json files in {json_file_path}")


def main():
    pass



if __name__ == '__main__':
    generate_json(5)
    
    
