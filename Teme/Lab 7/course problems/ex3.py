# 3 ---------------------------------------
import os
import sys

def get_total_size(dir_path = sys.argv[1]):
    total_size = 0
    try:
        for i in os.listdir(dir_path):
            i_path = os.path.join(dir_path, i)
            if(os.path.isdir(i_path)):
                total_size += get_total_size(i_path)
            else:
                total_size += os.path.getsize(i_path)
        return total_size
    except PermissionError:
        print("Permission error")
    except FileNotFoundError:
        print("Directory not existing")
    except:
        print("Other file access issues")

print(get_total_size())