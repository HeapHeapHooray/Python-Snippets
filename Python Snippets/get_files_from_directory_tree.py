import os
from typing import List

def get_files_from_directory_tree(directory_path: str) -> List[str]:
    full_path_files = []

    for root_path,directories,files in os.walk(directory_path):
        for file_name in files:
            full_path_files.append(os.path.join(root_path,file_name))

    return full_path_files
