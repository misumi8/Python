def countBits(number):
    return bin(number).count("1")

print(countBits(111)) # 1101111 = 6