import json

def split_json(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Load JSON data to ensure proper formatting
    try:
        json_data = json.loads(data)
        formatted_data = json.dumps(json_data, indent=4)
    except json.JSONDecodeError:
        print("Invalid JSON format in file:", file_path)
        return

    half_length = len(formatted_data) // 2
    part1 = formatted_data[:half_length]
    part2 = formatted_data[half_length:]

    # Write the split data to new files with part_1 and part_2 suffixes
    with open(file_path[:-5] + '_part_1.json', 'w') as part1_file:
        part1_file.write(part1)
    with open(file_path[:-5] + '_part_2.json', 'w') as part2_file:
        part2_file.write(part2)

# Example usage
split_json('custom_1.json')
