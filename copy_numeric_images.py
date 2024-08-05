import os
import shutil
import re

def is_numeric(filename):
    """Check if the filename (without extension) is numeric."""
    return re.match(r'^\d+$', os.path.splitext(filename)[0])

def copy_images_with_numeric_names(src, dst):
    """Copy images with numeric names from src to dst, preserving folder structure."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for root, dirs, files in os.walk(src):
        # Determine the destination path
        rel_path = os.path.relpath(root, src)
        dest_path = os.path.join(dst, rel_path)
        
        # Create directories in the destination path
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        
        for file in files:
            if is_numeric(file):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_path, file)
                shutil.copy2(src_file, dest_file)
                print(f"Copied {src_file} to {dest_file}")

# Source and destination directories
src_directory = '/var/www/a/img/img/p'
dst_directory = '/var/www/a/img/test'

copy_images_with_numeric_names(src_directory, dst_directory)
