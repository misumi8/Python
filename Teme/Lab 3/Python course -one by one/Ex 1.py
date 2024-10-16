# 1 -----------------------------------

def getFibSeq(n):
    fibList = []
    if (n < 0):
        return []
    if(n == 0):
        return [0]
    if(n == 1 or n == 2):
        return [0,1]

    fibList.append(0)
    fibList.append(1)
    for i in range(2, n + 1):
        fibList.append(fibList[i-1] + fibList[i-2])
    return fibList

list = getFibSeq(12)
for i in list:
    print(i, end = " ")