import os
import shutil


def create_subfolder_if_needed(folder_path, subfolder_name):
    """Create a subfolder if it does not already exist."""
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def clean_folder(folder_path):
    """Organize files in the given folder by moving them into subfolders based on their extensions."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            # Use os.path.splitext to get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lstrip('.').lower()  # Remove the leading dot and convert to lowercase

            if file_extension:  # Non-empty extension
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                shutil.move(file_path, os.path.join(subfolder_path, filename))
                print(f"Moved: {filename} -> {subfolder_name}/")
            else:  # No extension
                subfolder_name = "No Extension Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                shutil.move(file_path, os.path.join(subfolder_path, filename))
                print(f"Moved: {filename} -> {subfolder_name}/")


if __name__ == "__main__":
    print("Desktop Cleaner Script")
    folder_path = "/Users/arishmorani/downloads"

    if os.path.isdir(folder_path):
        try:
            clean_folder(folder_path)
            print("Cleaning complete.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again.")
