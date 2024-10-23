# 7 ------------------------------------------------
from pprint import pprint

def calcTwoByTwo(*sets):
    result = {}
    for i in range(0, len(sets) - 1, 2):
        result[str(sets[i]) + " | " + str(sets[i+1])] = sets[i].union(sets[i+1])
        result[str(sets[i]) + " & " + str(sets[i+1])] = sets[i].intersection(sets[i+1])
        result[str(sets[i]) + " - " + str(sets[i+1])] = sets[i].difference(sets[i+1])
        result[str(sets[i+1]) + " - " + str(sets[i])] = sets[i+1].difference(sets[i])
    return result

pprint(calcTwoByTwo({1,2}, {2,5}, {3,7},{2,9},{5,2}, {8,5}, {6,7},{1,9}))