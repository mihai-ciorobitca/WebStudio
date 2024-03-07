import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            new_filename = os.path.join(directory, filename.replace(".png", ".jpg"))
            os.rename(os.path.join(directory, filename), new_filename)
            print(f"Renamed {filename} to {os.path.basename(new_filename)}")

# Replace 'image_folder_path' with the path to your image folder
rename_files('images')
