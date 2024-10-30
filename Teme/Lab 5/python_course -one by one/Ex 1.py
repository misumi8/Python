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
