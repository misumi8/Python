# 9 -----------------------------------

def getUnluckySeats(spectators):
    unluckySeats = set()
    for i in range(0, len(spectators[0])):
        for j in range(0, len(spectators)):
            for k in range(j + 1, len(spectators)):
                if(spectators[j][i] >= spectators[k][i]):
                    unluckySeats.add((k, i))
    return list(unluckySeats)

unluckySeats = getUnluckySeats([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]])
for i in unluckySeats:
    print(i)
