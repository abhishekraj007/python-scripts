import os
import subprocess

def convert_videos_to_webp(input_dir, output_dir, frame_rate=10, quality=10, width=800):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get a list of all MP4 files in the input directory
    mp4_files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]

    for mp4_file in mp4_files:
        input_path = os.path.join(input_dir, mp4_file)
        output_path = os.path.join(output_dir, os.path.splitext(mp4_file)[0] + ".webp")

        # Convert MP4 to WebP using ffmpeg command
        try:
            print(f"Converting {mp4_file} to WebP...")
            subprocess.run([
                "ffmpeg",
                "-i", input_path,
                "-vf", f"scale={width}:-1",
                "-r", str(frame_rate),
                "-q:v", str(quality),
                "-loop", "0",
                output_path
            ], check=True)
            print(f"Conversion of {mp4_file} completed.")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mp4_file}: {e}")
            
if __name__ == "__main__":
    input_dir = os.path.expanduser('~/Documents/Apps/workout-assets/hips/animation')
    output_dir = os.path.expanduser('~/Documents/Apps/workout-assets/hips/animation')

    convert_videos_to_webp(input_dir, output_dir, frame_rate=30, quality=30, width=800)