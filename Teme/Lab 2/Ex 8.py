def getWordsCount(str):
    words = 0
    for i in str:
        if(i == " "):
            words = words + 1
    if(len(str) > 0):
        words = words + 1
    return words

# Another possible solution:
# def getWordsCount(str):
#     if(len(str) > 0):
#         return len(str.split(" "))
#     else:
#         return 0

print(getWordsCount("I have Python exam"))