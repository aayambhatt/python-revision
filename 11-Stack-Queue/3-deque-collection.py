from collections import deque

lst = deque()

lst.append(100)
lst.append(200)
lst.append(300)

print(lst)

lst.appendleft(50)
lst.append(400)

print(lst)