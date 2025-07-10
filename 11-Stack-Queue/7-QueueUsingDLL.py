class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class QueueUsingDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item):
        node1 = Node(item)
        if self.head is None:
            self.head = node1
            self.tail = node1
        else:
            self.tail.next = node1
            node1.prev = self.tail
            self.tail = node1
        self.size+=1

    def dequeue(self):
        if self.head is None:
            return -1
        
        popped_node = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        
        self.size -= 1
        return popped_node.data
            

    def front(self):
        if self.head:
            return self.head.data
        else:
            return -1

    def getSize(self):
        return self.size
