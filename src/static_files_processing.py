import os
import shutil

def create_public(destination_path):
    public_exists = os.path.exists(destination_path)
    print(f"Does {destination_path} exists: {public_exists}")

    if (public_exists):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)


def copy_static_to_public(src_path, destination_path):
    folder_content = os.listdir(src_path)
    print(f"Content of '{src_path}' folder: {folder_content}")
    for item in folder_content:
        full_src_path = os.path.join(src_path, item)
        print(full_src_path, os.path.isfile(full_src_path))
        if os.path.isfile(full_src_path):
            shutil.copy(full_src_path, os.path.join(destination_path, item))
        else:
            new_destination_path = os.path.join(destination_path, item)

            os.mkdir(new_destination_path)
            copy_static_to_public(full_src_path, new_destination_path)