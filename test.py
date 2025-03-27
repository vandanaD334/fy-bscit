import os
import shutil

def convert_file_extension(input_file, new_extension):
    """Convert a file to a new extension while keeping the content unchanged."""
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return
    
    file_name, _ = os.path.splitext(input_file)
    output_file = f"{file_name}.{new_extension.lstrip('.')}"  # Ensure no extra dot

    # Copy content to the new file
    shutil.copy(input_file, output_file)
    print(f"File converted: {input_file} → {output_file}")

# Example usage
input_path = "example.txt"  # Change this to your file
desired_extension = "csv"   # Change this to your desired extension

convert_file_extension(input_path, desired_extension)
