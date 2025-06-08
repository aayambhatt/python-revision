x = 10

def test():
    x = 5
    print("Inside:", x)

test()           # Inside: 5
print("Outside:", x)  # Outside: 10
