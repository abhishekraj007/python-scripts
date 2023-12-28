import os
import re

def rename_files(folder_path):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    for file_name in all_files:
        # change patterns here
        # Apply the renaming pattern using regular expressions
        # new_name = re.sub(r'\b\d+\b|\b\w{1}\b', '', file_name, flags=re.IGNORECASE)
        # new_name = re.sub(r'[_-]+', '_', new_name).strip('_').lower()

        # Apply the renaming pattern using regular expressions
        new_name = re.sub(r'\b\d+\b|\b\w{1}\b|\.\.\.', '', file_name, flags=re.IGNORECASE)
        new_name = re.sub(r'[_-]+', '_', new_name).strip('_').lower()


        # Construct the full paths for the old and new names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} to {new_name}")
        except Exception as e:
            print(f"Error renaming {file_name}: {e}")

if __name__ == "__main__":
    folder_path = os.path.expanduser('~/Documents/Apps/workout-assets/videos')

    rename_files(folder_path)
