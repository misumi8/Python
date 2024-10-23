# 2 ------------------------------------------------

def getCharOccur(string):
    occurs = {}

    for i in string:
        if(i not in occurs):
            occurs[i] = 1
        else:
            occurs[i] += 1
    return occurs

# print(getCharOccur("Ana has apples."))