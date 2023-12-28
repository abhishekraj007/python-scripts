import os

fileType = ".webp"

def delete_webp_files(folder_path):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Filter files with .webp extension
    webp_files = [file for file in all_files if file.lower().endswith(fileType)]

    # Delete each .webp file
    for webp_file in webp_files:
        file_path = os.path.join(folder_path, webp_file)
        try:
            os.remove(file_path)
            print(f"Deleted: {webp_file}")
        except Exception as e:
            print(f"Error deleting {webp_file}: {e}")

if __name__ == "__main__":
    folder_path = os.path.expanduser('~/Documents/Apps/workout-assets/videos')
    
    delete_webp_files(folder_path)
