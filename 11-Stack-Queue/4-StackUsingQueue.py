from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if len(self.queue)==0:
            return -1
        return self.queue.popleft()
    
    def top(self):
        if len(self.queue)==0:
            return -1
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    