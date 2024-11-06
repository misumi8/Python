# 4 --------------------------------------------------
import time

def find_hex_in_bin():
    with open("numbers.bin", "rb") as b:
        bdata = b.read()
        nums = set()
        for i in range(0, len(bdata), 4):
            nums.add(int.from_bytes(bdata[i:i+4], "little"))
    f_matrix = [[0] * 32 for x in range(32)]
    with open("search_for_numbers.txt", "r") as h:
        k = 0
        for i in range(0, 1024):
            hnum = h.readline()
            if(hnum):
                if(int(hnum, 16) in nums):
                    f_matrix[k // 32][k % 32] = 1
            k += 1
        # print(nums)
        return f_matrix

start_time = time.time()
m = find_hex_in_bin()
end_time = time.time()

for i in range(0, len(m)):
    for j in range(0, len(m[0])):
        print(m[i][j], end = " ")
    print()
print("Execution time:", round(end_time - start_time, 2), "s.")