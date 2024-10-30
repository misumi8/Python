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
