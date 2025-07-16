def xToN(x,N):
    if x > N:
        return

    print(x)
    xToN(x+1,N)

xToN(3,8)