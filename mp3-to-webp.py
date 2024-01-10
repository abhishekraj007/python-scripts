import os
import mutagen
from mutagen.id3 import ID3
from mutagen.id3 import PictureType
from PIL import Image
from io import BytesIO

def extract_cover_art(mp3_path, output_dir):
    audio = ID3(mp3_path)

    for key in audio.keys():
        if key.startswith('APIC:'):
            artwork = audio[key].data  # access APIC frame and grab the image
            img = Image.open(BytesIO(artwork))
            cover_path = os.path.join(output_dir, os.path.splitext(os.path.basename(mp3_path))[0] + '.webp')
            img.save(cover_path, 'WEBP', quality=10)

def process_directory(dir_path, output_dir):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.mp3'):
                extract_cover_art(os.path.join(root, file), output_dir)

# Replace with your directory path
                
input_folder = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/gym-tracks-2024')

output_folder = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/gym-tracks-2024/images')

process_directory(input_folder, output_folder)
