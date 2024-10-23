# 9 ------------------------------------------------

def func(*positionalArgs, **keywordArgs):
    count = 0
    for i in positionalArgs:
        if(i in keywordArgs.values()):
            count += 1
    return count

# print(func(1, 2, 3, 4, x=1, y=2, z=3, w=5))
