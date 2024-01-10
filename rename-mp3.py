import os
import re


playlist_name = 'workout-pop-hits'
playlist_folder = os.path.expanduser(f'~/Documents/Apps/workout-assets/playlists/{playlist_name}')

def transform_file_names(folder_path):
    for filename in os.listdir(folder_path):
        old_file_path = os.path.join(folder_path, filename)

        # Transform the filename
        new_filename = re.sub(r'[^\w\s.-]', '', filename)  # Remove special characters
        new_filename = re.sub(r'\s+', ' ', new_filename)  # Replace multiple spaces with a single space
        new_filename = new_filename.replace(' ', '-')  # Replace spaces with hyphens
        new_filename = re.sub(r'-+', '-', new_filename)  # Replace multiple dashes with a single dash
        new_file_path = os.path.join(folder_path, new_filename)

        # Rename the file
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {filename}: {str(e)}")

if __name__ == "__main__":

    transform_file_names(playlist_folder)
