def palindrome(x):
    num = x 
    res = 0

    while num > 0:
        ld = num % 10
        res = res * 10 + ld
        num = num // 10

    if res == x:
        return True
    else: 
        return False

print(palindrome(121))
print(palindrome(123))