def armstrong(x):
    num = x 
    total = 0
    nod = len(str(x))
    while num > 0:
        ld = num % 10
        total = total + (ld**nod)
        num = num // 10
    
    if x == total:
        return True
    else:
        return False

print(armstrong(153))
print(armstrong(125))