import os
import imageio

def convert_videos_to_webp(input_dir, output_dir, frame_rate=10, quality=10, width=800):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # while True:
    # Get a list of all MP4 files in the input directory
    mp4_files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]

    for mp4_file in mp4_files:
        input_path = os.path.join(input_dir, mp4_file)
        output_path = os.path.join(output_dir, os.path.splitext(mp4_file)[0] + ".webp")

        # Convert MP4 to WebP
        try:
            print(f"Converting {mp4_file} to WebP...")
            video_reader = imageio.get_reader(input_path)
            fps = video_reader.get_meta_data()['fps']

            # Calculate the height while maintaining the aspect ratio
            height = int(video_reader.get_meta_data()['size'][1] * (width / video_reader.get_meta_data()['size'][0]))

            video_writer = imageio.get_writer(output_path, format="webp", fps=frame_rate, quality=quality, width=width, height=height)

            for frame in video_reader:
                video_writer.append_data(frame)

            video_writer.close()
            print(f"Conversion of {mp4_file} completed.")
        except Exception as e:
            print(f"Error converting {mp4_file}: {e}")
            
if __name__ == "__main__":
    input_dir = os.path.expanduser('~/Documents/Apps/workout-assets/videos')
    output_dir = os.path.expanduser('~/Documents/Apps/workout-assets/videos/webp')

    convert_videos_to_webp(input_dir, output_dir, frame_rate=30, quality=20, width=800)