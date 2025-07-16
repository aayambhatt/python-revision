count = 0
def printName():
    global count
    if count == 4:
        return
    print("Aayam")
    count+=1
    printName()


printName()

