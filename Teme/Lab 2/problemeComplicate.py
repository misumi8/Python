# 8 (transferred from probleme simple) 

def generatePermutation(num):
    chars = 'AEGIJLNOPSUVbdefhimnoprstuvwxy'
    perm = ""
    while(num > 0):
        perm = chars[num % 30] + perm
        num = num // 30
    return perm

# print(generatePermutation(218553019))

# --------------------------------

def group(num, numOfDecimals):
    if(len(str(num)) % 2 == 0):
        result = str(num) + '00' * numOfDecimals
    else:
        result = '0' + str(num) + '00' * numOfDecimals
    return result

def func(num, numOfDecimals):
    groups = group(num, numOfDecimals)
    p = 0
    c = 0
    for i in range(len(groups) // 2):
        c = c * 100 + int(groups[i*2:(i+1)*2])
        for j in range(11):
            if(j * (20 * p + j) > c):
                break
        j = j - 1
        y = j * (20 * p + j)
        p = p * 10 + j
        c = c - y
    return p

# print(func(52,4))
# print(func(152,2))
# print(func(2,3000))