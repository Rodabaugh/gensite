import os
import shutil

def recursive_copy(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        try:
            print(f'Creating new {destination_directory} dir')
            os.mkdir(destination_directory)
        except Exception as error:
            raise Exception(f'Was unable to create new {destination_directory} dir:\n{error}')
    
    files = os.listdir(source_directory)
    for file in files:
        full_file_path = os.path.join(source_directory, file)
        new_file_path = os.path.join(destination_directory, file)
        if os.path.isfile(full_file_path):
            print(f"Copying {full_file_path} to {new_file_path}")
            try:
                shutil.copy(full_file_path, new_file_path)
            except Exception as error:
                print(f"Was unable to copy {full_file_path} to {new_file_path}:\n{error}")
        if os.path.isdir(full_file_path):
            recursive_copy(full_file_path, new_file_path)