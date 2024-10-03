# tga_2_png.py
#
# This script converts TGA image files to PNG format recursively within a specified project folder.
# It preserves folder structure and converts all TGA files found.
#
# Usage:
#   1. Run this script.
#   2. When prompted, enter the path to the project folder.
#
# Requirements:
#   - Python 3.x
#   - Dependencies: Pillow
#     Install dependencies using: pip install Pillow
#
# Author: Jolly Joe
# Date: 10/03/2024
# Version: 1.0

import os
from PIL import Image

def convert_gif_to_png(tga_file):
    try:
        # Check if the file exists
        if not os.path.exists(tga_file):
            raise FileNotFoundError(f"{tga_file} does not exist.")
        
        # Open the TGA image
        with Image.open(tga_file) as img:
            # Remove .GIF extension and add .png
            png_file = tga_file[:-4] + '.png'
            
            # Check if .png file already exists
            if os.path.exists(png_file):
                print(f"Skipping {tga_file} -> {png_file}: .png file already exists.")
                return
            
            # Save as PNG
            img.save(png_file)
            
        print(f"Converted {tga_file} to {png_file}")
    except Exception as e:
        print(f"Error converting {tga_file} to PNG: {e}")

def find_and_convert_gif_to_png(root_dir):
    try:
        for folder, _, files in os.walk(root_dir):
            for file_name in files:
                if file_name.lower().endswith('.tga'):
                    file_path = os.path.join(folder, file_name)
                    convert_gif_to_png(file_path)
    except Exception as e:
        print(f"Error processing files: {e}")

# Example usage
if __name__ == "__main__":
    root_directory = input("Folder you want to change tga > png\n:> ")  # Replace with your root directory
    
    # Check if the root directory exists
    if not os.path.exists(root_directory):
        print(f"Error: {root_directory} does not exist.")
    else:
        find_and_convert_gif_to_png(root_directory)
