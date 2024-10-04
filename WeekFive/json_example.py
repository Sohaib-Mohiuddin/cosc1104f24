import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def store_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
if __name__ == "__main__":
    # Load data from a JSON file
    input_file = 'input.json'
    data = load_json(input_file)
    print(data['first_name'])

    # Store data into a JSON file
    # output_file = 'input.json'
    # new_data = {
    #     "first_name": "John",
    #     "last_name": "Doe",
    #     "age": 30
    # }
    # store_json(output_file, new_data)