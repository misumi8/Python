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