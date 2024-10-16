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

groups = groupWordsByRhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
for group in groups:
    for i in group:
        print(i, end = " ")
    print()