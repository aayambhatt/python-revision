def sumN(total, i, N):
    if i >N:
        print(total)
        return
    sumN(total+i, i+1, N)

sumN(0, 1, 4)
