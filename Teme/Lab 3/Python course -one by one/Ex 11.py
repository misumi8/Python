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

tuples = orderBy3rdCharOf2ndElement([('abc','bcd'), ('abc', 'zza'), ('aaa', 'aaz'), ('zzz', 'zzz')])
for i in tuples:
    print(i, end = " ")
