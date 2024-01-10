import os
import json
import uuid
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from PIL import Image
from io import BytesIO
import re
import mutagen
from mutagen.mp3 import MP3


playlist_name = 'workout-pop-hits'

mp3_base_url = f'https://raw.githubusercontent.com/abhishekraj007/workout-assets/main/playlists/{playlist_name}/'
image_base_url = f'https://raw.githubusercontent.com/abhishekraj007/workout-assets/main/playlists/{playlist_name}/images/'

playlist_folder = os.path.expanduser(f'~/Documents/Apps/workout-assets/playlists/{playlist_name}')

output_dir = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/json')
image_dir = os.path.join(playlist_folder, 'images')

max_duration = 600 #mins

def extract_metadata(directory):
    data = []
    os.makedirs(image_dir, exist_ok=True)
    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            path = os.path.join(directory, filename)
            audio = MP3(path, ID3=ID3)

            # Generate a UUID
            track_id = str(uuid.uuid4())

            # Extract metadata
            name = audio['TIT2'].text[0] if 'TIT2' in audio else ''

            duration = audio.info.length  # duration in seconds
            print(f"Duration: {duration} : {name}")
            if duration > max_duration:
                os.remove(path)
                print(f'Deleted file: {path}')

            if name:  # Only append metadata if 'name' is not empty
                image_filename = f"{os.path.splitext(filename)[0]}.webp"
                mp3_url = mp3_base_url + filename
                image_url = image_base_url + image_filename

                metadata = {
                    'duration': audio.info.length,
                    'id': track_id,
                    'name': name,
                    'artist': audio['TPE1'].text[0] if 'TPE1' in audio else '',
                    'album': audio['TALB'].text[0] if 'TALB' in audio else '',
                    'url': mp3_url,
                    'image': image_url
                }

                print('saving metadata...')
                data.append(metadata)

                for key in audio.keys():
                    if key.startswith('APIC:'):
                        artwork = audio[key].data  # access APIC frame and grab the image
                        img = Image.open(BytesIO(artwork))
                        cover_path = os.path.join(image_dir, os.path.splitext(os.path.basename(path))[0] + '.webp')
                        # print('saving', cover_path)
                        img.save(cover_path, 'WEBP', quality=10)

    # Load existing JSON structure from the file
    json_filename = os.path.join(output_dir, f'{playlist_name}.json')
    existing_data = {}
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as json_file:
            existing_data = json.load(json_file)

    # Update the 'tracks' property with the new data
    if 'tracks' not in existing_data:
        existing_data['tracks'] = []

    existing_data['tracks'] = data

    # Save the updated data to the JSON file
    with open(json_filename, 'w') as f:
        json.dump(existing_data, f, indent=4)

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

transform_file_names(playlist_folder)
extract_metadata(playlist_folder)
