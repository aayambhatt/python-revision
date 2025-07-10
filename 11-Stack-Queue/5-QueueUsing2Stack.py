class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, item):
        # Move all elements from st1 to st2
        while self.st1:
            self.st2.append(self.st1.pop())

        # Push item to st1
        self.st1.append(item)

        # Move everything back to st1
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            return -1
        return self.st1.pop()

    def top(self):
        if not self.st1:
            return -1
        return self.st1[-1]

    def isEmpty(self):
        return len(self.st1) == 0
