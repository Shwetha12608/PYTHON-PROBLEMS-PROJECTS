import os

source_file_path = input("Enter the source file path: ")
destination_file_path = input("Enter the destination file path: ")

if os.path.exists(source_file_path):
    with open(source_file_path, 'r', encoding='utf-8', errors='replace') as src:
        content = src.read()
    with open(destination_file_path, 'w', encoding='utf-8') as dest:
        dest.write(content)
    print("Content copied successfully.")
else:
    print(f"Source file {source_file_path} does not exist.")
