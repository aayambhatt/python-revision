class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items)==0:
            return "Stack is empty"
        x = self.items.pop()
        return x

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)



    