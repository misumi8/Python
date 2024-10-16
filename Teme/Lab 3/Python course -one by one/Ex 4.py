# 4 -----------------------------------

def composeSong(notes, moves, startPosition):
    song = notes[startPosition] + " "
    position = startPosition
    for i in moves:
        position = (position + i) % len(notes)
        song += notes[position] + " "
    return song

print(composeSong(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
