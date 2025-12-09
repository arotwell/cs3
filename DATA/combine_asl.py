import os
import shutil

# Combine images from all users into a single folder structure
# Should work if the ASLYset folder is in the same directory as this script

# === Configuration ===
root_dir = "ASLYset"
src_root = os.path.join(root_dir, "images")
dest_root = os.path.join(root_dir, "asl_data")

# Make sure the destination folder exists
os.makedirs(dest_root, exist_ok=True)

# Loop through all user folders (User1, User2, etc.)
for user_dir in os.listdir(src_root):
    user_path = os.path.join(src_root, user_dir)
    if not os.path.isdir(user_path):
        continue

    # Loop through A–Y, SP, FN (whatever subfolders exist)
    for letter_dir in os.listdir(user_path):
        letter_path = os.path.join(user_path, letter_dir)
        if not os.path.isdir(letter_path):
            continue

        # Create the corresponding folder in combined_images/
        dest_letter_dir = os.path.join(dest_root, letter_dir.upper())
        os.makedirs(dest_letter_dir, exist_ok=True)

        # Copy all image files
        for filename in os.listdir(letter_path):
            src_file = os.path.join(letter_path, filename)
            if os.path.isfile(src_file):
                dest_file = os.path.join(dest_letter_dir, filename)
                shutil.copy(src_file, dest_file)

print("All user images combined successfully into", dest_root)
