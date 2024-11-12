# 1 ---------------------------------------
import sys
import os
from pprint import pprint


def get_format_files_content(directory_path, file_extension):
    try:
        assert(file_extension.startswith(".") and file_extension.count(".") == 1), "Incorrect file extension"
        files = {}
        for i in os.listdir(directory_path):
            print(i)
            i_path = os.path.join(directory_path, i)
            if(os.path.isdir(i_path)):
                files = files | get_format_files_content(i_path, file_extension)
            else:
                if(i_path.split(".")[-1] == file_extension.lstrip(".")):
                    with open(directory_path + "\\" + i, "r") as f:
                        files[directory_path + "\\" + i] = f.read()
        return files
    except FileNotFoundError:
        print("Invalid directory path")
    except PermissionError:
        print("File access error")

pprint(get_format_files_content(sys.argv[1], sys.argv[2])) # sys.argv[2]