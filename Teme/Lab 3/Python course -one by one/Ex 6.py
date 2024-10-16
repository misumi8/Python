# 6 -----------------------------------

def getItemsByAppearances(appearances, *lists):
    items = set()
    concatenatedLists = []
    for list in lists:
        concatenatedLists += list
    for i in concatenatedLists:
        count = 0
        for j in concatenatedLists:
            if(i == j):
                count += 1
        if(count == appearances):
            items.add(i)
    return items

items = getItemsByAppearances(2, [1,2,3], [2,3,4],[4,5,6], [4,1, "test"])
for i in items:
    print(i, end = " ")
