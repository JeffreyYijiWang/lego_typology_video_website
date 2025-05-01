import os

def rename_files_in_folder(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out non-files (directories)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort files to ensure consistency in renaming order
    files.sort()

    # Rename each file
    for index, file_name in enumerate(files, start=1):
        file_extension = file_name.split('.')[-1]
        new_name = f"{index}.png"  # Rename to the new index-based name
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {file_name} to {new_name}")

# Example usage
folder_path = r"C:\Users\Jeffr\OneDrive\Documents\GitHub\lego_typology_video_website\mapImages" 
rename_files_in_folder(folder_path)
