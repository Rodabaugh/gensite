import os
import shutil

from copy_static import recursive_copy
from generate_content import generate_page

def main():
    if os.path.exists("public"):
            print('Removing exisiting "Public" dir')
            try:
                shutil.rmtree("public")
            except Exception as error :
                raise Exception(f'Was unable to delete "Public" dir:\n{error}')
    
    recursive_copy()
    generate_page("public/content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()