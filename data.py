from os import path
import json

def create_data():
    print("tasks.json not found; creating file now.")
    file = "tasks.json"
    try:
        with open(file, 'w') as tasks:
            data = '{"id_counter": 1, "tasks": [{"id": 1, "label": "Write your first task"}]}'
            tasks.write(data)
        
        print(f"File '{file}' created successfully.")
    except OSError as e:
        print(f"Error creating file '{file}': {e}")


def load_data():
    if not path.isfile("tasks.json"):
        create_data()

    with open("./tasks.json", 'r') as f:
        db = json.load(f)

    return db


def save_data(data):
    with open("tasks.json", 'w') as f:
        f.write(data)

    return 0
