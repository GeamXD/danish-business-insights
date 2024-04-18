import os

# Directory containing the files
directory = '/workspace/danish-business-insights/jsons'

# List all files in the directory
files = os.listdir(directory)



# Sort the files based on their timestamps
sorted_files = sorted(files)

# Counter for renaming
counter = 1

# Iterate through the sorted files
for file_name in sorted_files:
    # Check if the file is a JSON file
    if file_name.endswith('.json'):
        # Rename the file to json_data_<counter>.json
        new_file_name = f'json_data_{counter}.json'
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
        counter += 1
