import json

def process_json_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        output_file.write("[\n")  # Start of JSON array
        for line in input_file:
            try:
                entry = json.loads(line)
                json.dump(entry, output_file)
                output_file.write(",\n")  # Add comma between JSON objects
            except json.JSONDecodeError:
                print("Invalid JSON format in line:", line)
                continue
        output_file.seek(-2, 1)  # Remove the last comma
        output_file.write("\n]")  # End of JSON array

# Example usage
process_json_file('custom_1.json', 'test.json')
