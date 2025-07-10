class MinStack:

    def __init__(self):
        self.st1 = []
        self.minSt = []
        
        

    def push(self, val: int) -> None:
        self.st1.append(val)

        if not self.minSt:
            self.minSt.append(val)
        else:
            current_mini = self.minSt[-1]
            self.minSt.append(min(val, current_mini))
       
    def pop(self) -> None:
        if self.st1:
            self.st1.pop()
            self.minSt.pop()

    def top(self) -> int:
        return self.st1[-1]
        
        

    def getMin(self) -> int:
        return self.minSt[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()