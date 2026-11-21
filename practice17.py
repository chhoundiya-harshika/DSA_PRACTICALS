# from collections import deque

# queue = deque()

# queue.append(9)
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)
# queue.popleft()
# print(queue)
# print(queue[0])


from collections import deque
class Queue:
    def __init__(self):
        self.items=deque()
    def enqueue(self, value):
        self.items.append(value)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

q=Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.size())
print(q.is_empty())
            
        