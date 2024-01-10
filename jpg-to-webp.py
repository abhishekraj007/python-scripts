import os
from PIL import Image

output_dir = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/gym-tracks-2024/images/webp')

def convert_and_compress_images(directory):
    for filename in os.listdir(directory):

        if filename.endswith(".jpg"):
            
            img = Image.open(os.path.join(directory, filename))
            print(f"Converting {img} to WebP...")
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            img.save(os.path.join(directory, webp_filename), "WEBP", quality=10)
            
if __name__ == "__main__":
    # Specify the folder path
    folder_path = os.path.expanduser('~/Documents/Apps/workout-assets/playlists/gym-tracks-2024/images')

    convert_and_compress_images(folder_path)