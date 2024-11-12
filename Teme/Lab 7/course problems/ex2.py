# 2 ---------------------------------------
import os

def rename_files(dir_path):
    k = 0
    try:
        for i in os.listdir(dir_path):
            i_path = os.path.join(dir_path, i)
            if(os.path.isdir(i_path)):
                rename_files(i_path)
            else:
                i_split = os.path.splitext(i)
                os.rename(i_path, i_path.rstrip(i) + i_split[0] + str(k) + i_split[1])
                k += 1
    except FileNotFoundError:
        print("Directory not existing")
    except PermissionError:
        print("File can't be renamed")

rename_files("A://TEMP")