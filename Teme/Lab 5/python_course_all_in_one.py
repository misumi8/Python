# 1 --------------------------------------------------

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if(not self.stack):
            return None
        removed_item = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return removed_item

    def peek(self):
        if (not self.stack):
            return None
        return self.stack[len(self.stack) - 1]

# s = Stack()
# print(s.peek())
# print(s.pop())
# s.push(10)
# s.push(11)
# s.push(74)
# print(s.stack)
# print(s.peek())
# print(s.pop())
# print(s.peek())
# print(s.stack)

# 2 --------------------------------------------------

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if (not self.queue):
            return None
        removed_item = self.queue[0]
        del self.queue[0]
        return removed_item

    def peek(self):
        if (not self.queue):
            return None
        return self.queue[0]

# q = Queue()
# print(q.peek())
# print(q.pop())
# q.push(10)
# q.push(11)
# q.push(74)
# print(q.queue)
# print(q.peek())
# print(q.pop())
# print(q.peek())
# print(q.queue)

# 3 --------------------------------------------------

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for i in range(n)]

    def get(self, x, y):
        return self.matrix[x][y]

    def set(self, x, y, item):
        self.matrix[x][y] = item

    def transpose(self):
        transposed_matrix = [[0] * self.n for i in range(self.m)]
        for i in range(0, self.n):
            for j in range(0, self.m):
                transposed_matrix[j][i] = self.matrix[i][j]
        self.n, self.m = self.m, self.n
        self.matrix = transposed_matrix

    def multiply(self, matrix):
        if(not len(self.matrix[0]) == len(matrix)):
            return None
        mul_matrix = [[0] * len(matrix[0]) for i in range(0, len(self.matrix))]
        for i in range(0, len(self.matrix)):
            for j in range(0, len(matrix[0])):
                mul_matrix[i][j] = sum([self.matrix[i][k] * matrix[k][j] for k in range(0, len(self.matrix[0]))])
        self.matrix = mul_matrix
        self.n = len(mul_matrix)
        self.m = len(mul_matrix[0])

    def modify_elements(self, lambda_function):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                self.matrix[i][j] = lambda_function(self.matrix[i][j])

# m = Matrix(2,3)
# m.matrix = [[1,2,3], [4,5,6]]
# m.multiply([[7,8],[9,10],[11,12]])
# print(m.matrix)
# m.modify_elements(lambda x: x * x)
# print(m.matrix)
# m.transpose()
# print(m.matrix)
# m.transpose()
# print(m.get(0,0))
# m.set(0,0, 5)
# print(m.get(0,0))
# print(m.matrix)
