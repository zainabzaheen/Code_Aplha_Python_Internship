#import .jpg files from source folder to new folder

import os
import shutil

                # Moves all files from source_folder to destination_folder.Creates destination_folder if it doesn't exist.
def move_files (source_folder, new_folder): 

    try:
        if not os.path.exists(source_folder):
            print(f"Error: Source folder '{source_folder}' does not exist.")
            return
            
        # Create destination folder if it doesn't exist
        os.makedirs(new_folder,exist_ok=True)

        # Loop through all files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(new_folder, filename)

            # Move only files (skip subdirectories)
            if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
        
        print("All files moved successfully.")

    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
source = "Test_Folder"       # Replace with your source folder path
destination = "new_folder"  # Replace with your destination folder path

print("Python is running from:", os.getcwd())
print("Destination will be:", os.path.abspath(destination))
move_files(source, destination)