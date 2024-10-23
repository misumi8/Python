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
