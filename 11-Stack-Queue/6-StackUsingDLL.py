# Node class for DLL
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Stack using DLL
class StackUsingDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def push(self, item):
        node1 = Node(item)
        if self.head is None:
            self.head = node1
            self.tail = node1
        else:
            self.tail.next = node1
            node1.prev = self.tail
            self.tail = node1
        self.size += 1

    def pop(self):
        if self.tail is None:
            return "Stack is empty"

        popped_node = self.tail
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        self.size -= 1
        return popped_node.data

    def top(self):
        if self.tail:
            return self.tail.data
        else:
            return "Stack is empty"

    def getSize(self):
        return self.size
