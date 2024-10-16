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

# list = getFibSeq(12)
# for i in list:
#     print(i, end = " ")

# 2 -----------------------------------

def isPrime(num):
    if(num < 2):
        return False
    for i in range(2, num // 2 + 1):
        if(num % i == 0):
            return False
    return True

def findPrimeNumbers(list):
    newList = []
    for i in list:
        if(isPrime(i)):
            newList.append(i)
    return newList

# newList = findPrimeNumbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
# for i in newList:
#     print(i)

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

#print(calc([12,33,55], [11,20,33,21,12]))

# 4 -----------------------------------

def composeSong(notes, moves, startPosition):
    song = notes[startPosition] + " "
    position = startPosition
    for i in moves:
        position = (position + i) % len(notes)
        song += notes[position] + " "
    return song

# print(composeSong(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# 5 -----------------------------------

def clearDiagonal(matrix):
    #if(len(matrix) != len(matrix[0])):
    #    raise Exception("Not a square matrix => no diagonal")
    for i in range(0, min(len(matrix), len(matrix[0]))):
        matrix[i][i] = 0
    return matrix

# matrix = clearDiagonal([[1,2,3,13],[4,5,6,14],[7,8,9,15], [4,7,5,16]])
# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix[i])):
#         print(matrix[i][j], end = "  ")
#     print()

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

# items = getItemsByAppearances(2, [1,2,3], [2,3,4],[4,5,6], [4,1, "test"])
# for i in items:
#     print(i, end = " ")

# 7 -----------------------------------

def isPalindrome(number):
    reversed = 0
    numberCpy = number
    numberCpy2 = number
    step = 1
    while(numberCpy > 0):
        numberCpy = numberCpy // 10
        step = step * 10
    step = step // 10
    while(number > 0):
        reversed = reversed + ((number % 10) * step)
        number = number // 10
        step = step // 10
    return reversed == numberCpy2

def getCountAndGreatestPalindrome(nums):
    count = 0
    greatest = -1
    for num in nums:
        if(isPalindrome(num)):
            count += 1
            if(num > greatest):
                greatest = num
    if(count == 0):
        return (count, "None")
    return (count, greatest)

# print(getCountAndGreatestPalindrome([80, 746, 101, 111, 110, 131, 141]))

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

# lists = getCharsByDivision(["test", "hello", "lab002"], 2, False)
# for list in lists:
#     for i in list:
#         print(i, end = " ")
#     print()

# 9 -----------------------------------

def getUnluckySeats(spectators):
    unluckySeats = set()
    for i in range(0, len(spectators[0])):
        for j in range(0, len(spectators)):
            for k in range(j + 1, len(spectators)):
                if(spectators[j][i] >= spectators[k][i]):
                    unluckySeats.add((k, i))
    return list(unluckySeats)

# unluckySeats = getUnluckySeats([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]])
# for i in unluckySeats:
#     print(i)

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

#print(getTuplesFromLists([1,2,3], [5,6,7], ["a", "b", "c"]))

# 11 -----------------------------------

def sortBy(e):
    if(len(e) < 2):
        raise Exception("The tuple must contain at least 2 items")
    elif(len(e[1]) < 3):
        raise Exception("The length of the 2nd item must be at least 3")
    return ord(e[1][2].lower()) # if we need to sort by ascii code we can remove .lower()

def orderBy3rdCharOf2ndElement(tuples):
    tuples.sort(key = sortBy)
    return tuples

# tuples = orderBy3rdCharOf2ndElement([('abc','bcd'), ('abc', 'zza'), ('aaa', 'aaz'), ('zzz', 'zzz')])
# for i in tuples:
#     print(i, end = " ")

# 12 -----------------------------------

def groupWordsByRhyme(words):
    groupedList = []
    usedWords = set()
    for i in range(0, len(words)):
        if(words[i] not in usedWords):
            group = [words[i]]
            usedWords.add(words[i])
            for j in range(i + 1, len(words)):
                if(words[i][-1] == words[j][-1] and words[i][-2] == words[j][-2]):
                    group.append(words[j])
                    usedWords.add(words[j])
            groupedList.append(group)
    return groupedList

# groups = groupWordsByRhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
# for group in groups:
#     for i in group:
#         print(i, end = " ")
#     print()