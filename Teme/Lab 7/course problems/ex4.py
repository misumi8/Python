# 4 ---------------------------------------
import os
import sys

def get_ext_counts(dir_path = sys.argv[1]):
    counts = {}
    try:
        if(len(os.listdir(dir_path)) < 1):
            raise Exception(f"[{dir_path}] Directory is empty")
        for i in os.listdir(dir_path):
            i_path = os.path.join(dir_path, i)
            if(os.path.isdir(i_path)):
                try:
                    new_counts = get_ext_counts(i_path)
                    for i in new_counts:
                        if (i not in counts):
                            counts[i] = 0
                        counts[i] += new_counts[i]
                except Exception as e:
                    print(f"[{i_path}] {str(e)}")
            else:
                if(os.path.splitext(i)[1] not in counts):
                    counts[os.path.splitext(i)[1]] = 0
                counts[os.path.splitext(i)[1]] += 1
        return counts
    except PermissionError:
        print("Permission error")
        return counts
    except FileNotFoundError:
        print("Directory not found")
        return counts
    except Exception as e:
        print(str(e))
        return counts

counts = get_ext_counts()
for k in counts:
    print(f"{k}: {counts[k]}")
