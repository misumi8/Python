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
