# Probleme grele
# 1 --------------------------------

import json
with open("Studenti.json") as f:
    data = json.load(f)
max = 400
studentiTrecut = 0
studentiPicat = 0

for student in data.values():
    seminar = sum(student['seminarii'])
    examen = student['partial'] + student['curs']
    proiect = student['proiect']

    total = seminar + examen + proiect
    if (total/max >= 0.45):
        studentiTrecut += 1
    else:
        studentiPicat += 1

# print("Au trecut: ", studentiTrecut, "\nAu picat:", studentiPicat)

# 2 --------------------------------

import os
import json
from operator import itemgetter

def createJsonFile(name, data):
    data = sorted(data, key=itemgetter(1))
    with open("json/upTo" + str(name) + ".json", "w") as j:
        json.dump(data, j, indent=4)

def scanDisk(dir = "A:/"):
    groups = {}
    for root, dirs, files in os.walk(dir):
        for file in files:
            filePath = os.path.join(root, file)
            fileSizeMb = os.path.getsize(filePath) / 1000000
            if(fileSizeMb >= 200 and len(groups) < 30):
                group = 300
                initialSizeMb = fileSizeMb
                fileSizeMb -= 300
                while(fileSizeMb > 0):
                    fileSizeMb -= 300
                    group += 300
                if(group not in groups):
                    groups[group] = []
                groups[group].append((filePath, str(initialSizeMb) + " MB"))
    for k in groups.keys():
        createJsonFile(k, groups[k])

    for i in sorted(groups.keys()):
        print(i, end=" ")
    print()
    for j in range(1, len(groups.keys()) + 1):
        for i in sorted(groups.keys()):
            if(len(groups[i]) > 0):
                print("o", end=" " * (len(str(i))))
                groups[i].pop()
            else:
                print(".", end=" " * (len(str(i))))
        print(" |  " + str(j))

# scanDisk()

# 3 --------------------------------

import json

def getCaptcha(file = "date_captcha/00002.json"):
    with open(file, "r") as j:
        data = json.load(j)
    lastPixelDistance = 0
    usedChars = set()
    captcha = {}
    for i in range(5):
        minDistanceFound = float('inf')
        for char, values in data.items():
            for pos in data[char]:
                if(lastPixelDistance < pos[2] and minDistanceFound > pos[2] and char not in usedChars and pos[2] >= lastPixelDistance + 30):
                    minDistanceFound = pos[2]
                    xOffset = pos[0]
                    charToAdd = char
        captcha[xOffset] = charToAdd
        lastPixelDistance = minDistanceFound
        usedChars.add(charToAdd)
    sortedCaptcha = sorted(captcha.items())
    strCaptcha = ""
    for k, v in sortedCaptcha:
        strCaptcha += v
    return strCaptcha

# for i in range(1, 21):
#     print(getCaptcha("date_captcha/" + str(i).zfill(5) + ".json"))







