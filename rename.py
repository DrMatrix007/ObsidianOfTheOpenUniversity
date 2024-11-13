import os
import re

def rename_files_recursively(directory):
    # Define the pattern to match filenames like "<number> ממן"
    pattern = re.compile(r"ממן (\d+).pdf")

    # Walk through all subdirectories and files in the given directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if filename matches the pattern
            match = pattern.match(filename)
            if match:
                # Extract the number from the filename
                number = match.group(1)
                # Create the new filename
                new_filename = f"Mamman {number}{os.path.splitext(filename)[1]}"
                # Get full file paths
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                # Print only the files that were renamed
                print(f'Renamed: "{old_file_path}" to "{new_file_path}"')

# Use the current directory for recursive renaming
directory = '.'
rename_files_recursively(directory)
