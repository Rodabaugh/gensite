import os
import shutil

from copy_static import recursive_copy

def main():
    if os.path.exists("public"):
            print('Removing exisiting "Public" dir')
            try:
                shutil.rmtree("public")
            except Exception as error :
                raise Exception(f'Was unable to delete "Public" dir:\n{error}')
    recursive_copy()


if __name__ == "__main__":
    main()
