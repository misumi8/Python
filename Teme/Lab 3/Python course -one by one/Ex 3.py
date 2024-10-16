# 3 -----------------------------------

def calc(a, b):
    aSet = set(a)
    bSet = set(b)
    intersection = aSet.intersection(bSet)
    union = aSet.union(bSet)
    aDifB = aSet.difference(bSet)
    bDifA = bSet.difference(aSet)
    toReturn = "A intersected with B: "
    for i in intersection:
        toReturn += str(i) + " "
    toReturn += "\nA reunited with B: "
    for i in union:
        toReturn += str(i) + " "
    toReturn += "\nA - B: "
    for i in aDifB:
        toReturn += str(i) + " "
    toReturn += "\nB - A: "
    for i in bDifA:
        toReturn += str(i) + " "
    return toReturn

print(calc([12,33,55], [11,20,33,21,12]))
