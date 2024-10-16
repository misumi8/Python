# 5 -----------------------------------

def clearDiagonal(matrix):
    #if(len(matrix) != len(matrix[0])):
    #    raise Exception("Not a square matrix => no diagonal")
    for i in range(0, min(len(matrix), len(matrix[0]))):
        matrix[i][i] = 0
    return matrix

matrix = clearDiagonal([[1,2,3,13],[4,5,6,14],[7,8,9,15], [4,7,5,16]])
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end = "  ")
    print()
