# 1 ------------------------------------------------

def calc(a, b):
    aSet = set(a)
    bSet = set(b)
    intersection = aSet.intersection(bSet)
    union = aSet.union(bSet)
    aDifB = aSet.difference(bSet)
    bDifA = bSet.difference(aSet)
    resultStr = "A intersected with B: "
    for i in intersection:
        resultStr += str(i) + " "
    resultStr += "\nA reunited with B: "
    for i in union:
        resultStr += str(i) + " "
    resultStr += "\nA - B: "
    for i in aDifB:
        resultStr += str(i) + " "
    resultStr += "\nB - A: "
    for i in bDifA:
        resultStr += str(i) + " "
    return resultStr

# print(calc([12,33,55], [11,20,33,21,12]))