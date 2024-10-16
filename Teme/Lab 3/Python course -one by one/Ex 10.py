# 10 -----------------------------------

def getTuplesFromLists(*lists):
    tuples = []
    maxLength = 0
    for list in lists:
        if(len(list) > maxLength):
            maxLength = len(list)
    for i in range(0, maxLength):
        elements = []
        for list in lists:
            if(len(list) < i + 1):
                elements.append(None)
            else:
                elements.append(list[i])
        tuples.append(tuple(elements))
    return tuples

print(getTuplesFromLists([1,2,3], [5,6,7], ["a", "b", "c"]))
