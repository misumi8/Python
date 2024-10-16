# 8 -----------------------------------

def getCharsByDivision(strings, x = 1, flag = True):
    listOfLists = []
    for string in strings:
        listOfChars = []
        for i in string:
            if(flag and ord(i) % x == 0):
                listOfChars.append(i)
            elif(not flag and ord(i) % x != 0):
                listOfChars.append(i)
        listOfLists.append(listOfChars)
    return listOfLists

lists = getCharsByDivision(["test", "hello", "lab002"], 2, False)
for list in lists:
    for i in list:
        print(i, end = " ")
    print()
