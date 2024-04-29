import os
import shutil

from copy_static import recursive_copy
from generate_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if os.path.exists(dir_path_public):
            print(f'Removing exisiting {dir_path_public} dir')
            try:
                shutil.rmtree(dir_path_public)
            except Exception as error :
                raise Exception(f'Was unable to delete "Public" dir:\n{error}')
    
    recursive_copy(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


if __name__ == "__main__":
    main()