# 1 ------------------------------------------------
from enum import unique
from pprint import pprint


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

# 3 ------------------------------------------------

def compareDict(dict1, dict2):
    if(isinstance(dict1, dict) and isinstance(dict2, dict)):
        if(dict1.keys() != dict2.keys()):
            return False
        for k in dict1:
            if(not compareDict(dict1[k], dict2[k])):
                return False
    elif(isinstance(dict1, list) and isinstance(dict2, list)):
        if (len(dict1) != len(dict2)):
            return False
        for j in range(0, len(dict1)):
            if(not compareDict(dict1[j], dict2[j])):
                return False
    elif (isinstance(dict1, set) and isinstance(dict2, set)):
        if (len(dict1) != len(dict2)):
            return False
        for item in dict1:
            if (item not in dict2):
                return False
    else:
        return dict1 == dict2
    return True

# print(compareDict({
#     'a': 1,
#     'b': {48: 'abc', 84: 'cba'},
#     'c': [[48, [4848], 48]]
# }, {
#     'a': 1,
#     'b': {48: 'abc', 84: 'cba'},
#     'c': [[48, [4848], 48]]
# }))

# 4 ------------------------------------------------

def buildXmlElement(tag, content, **keyValueElements):
    xmlElement = "<" + tag
    for name, value in keyValueElements.items():
        xmlElement += " " + name + "=\"" + value + "\""
    xmlElement += ">" + content + "</" + tag + ">"
    return xmlElement

# print(buildXmlElement("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

# 5 ------------------------------------------------

def validateDict(setOfTuples, dictionary):
    for k, v in dictionary.items():
        isFound = False
        for i in setOfTuples:
            if(k == i[0]):
                if(len(i) < 4):
                    return False
                isFound = True
                if(not v.startswith(i[1])):
                    print("v not starts with i[1] |\"" + v + "\"|", i[1])
                    return False
                if(i[2] in v):
                    if((v.startswith(i[2]) or v.endswith(i[2])) and i[2] != ""):
                        print("v not contains i[2] |\"" + v + "\"|", i[2])
                        return False
                if(not v.endswith(i[3])):
                    print("v not ends with i[3] |\"" + v + "\"|", i[3])
                    return False
        if(not isFound):
            return False
    return True

# print(validateDict({
#     ("key1", "", "inside", ""),
#     ("key2", "start", "middle", "winter")
# },
#     {
#     "key1": "come inside, it's too cold out",
#     "key2": "start with the beginning, then middle, then winter"
# }))

# 6 ------------------------------------------------

def getCountOfUniqueAndDuplicate(nums):
    uniqueNums = set(nums)
    return len(uniqueNums), len(nums) - len(uniqueNums)

# print(getCountOfUniqueAndDuplicate([1,2,1,2,1,1,3,2,2,3,3,4,4,5,6,6,5]))

# 7 ------------------------------------------------

def calcTwoByTwo(*sets):
    result = {}
    for i in range(0, len(sets) - 1, 2):
        result[str(sets[i]) + " | " + str(sets[i+1])] = sets[i].union(sets[i+1])
        result[str(sets[i]) + " & " + str(sets[i+1])] = sets[i].intersection(sets[i+1])
        result[str(sets[i]) + " - " + str(sets[i+1])] = sets[i].difference(sets[i+1])
        result[str(sets[i+1]) + " - " + str(sets[i])] = sets[i+1].difference(sets[i])
    return result

# pprint(calcTwoByTwo({1,2}, {2,5}, {3,7},{2,9},{5,2}, {8,5}, {6,7},{1,9}))

# 8 ------------------------------------------------

def findCyclePath(mapping):
    cicleSet = set()
    start = mapping['start']
    path = []
    while(start not in cicleSet):
        path.append(start)
        cicleSet.add(start)
        start = mapping[start]
    return path

# print(findCyclePath({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

# 9 ------------------------------------------------

def func(*positionalArgs, **keywordArgs):
    count = 0
    for i in positionalArgs:
        if(i in keywordArgs.values()):
            count += 1
    return count

# print(func(1, 2, 3, 4, x=1, y=2, z=3, w=5))
