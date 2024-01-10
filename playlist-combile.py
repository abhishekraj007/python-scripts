import os
import json

def combine_json_files(input_folder, output_folder):
    combined_data = []

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_file_path = os.path.join(input_folder, filename)
            with open(input_file_path, 'r') as file:
                data = json.load(file)
                combined_data.append(data)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Write the combined data to 'final.json' in the output folder
    output_file_path = os.path.join(output_folder, 'final.json')
    with open(output_file_path, 'w') as output_file:
        json.dump(combined_data, output_file, indent=2)

if __name__ == "__main__":
    # Replace 'input_folder_path' with the actual path of your input folder containing JSON files
    input_folder_path = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/json')

    # Replace 'output_folder_path' with the desired path for the output folder
    output_folder_path = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/json/final')

    combine_json_files(input_folder_path, output_folder_path)
