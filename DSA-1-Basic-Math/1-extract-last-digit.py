def last_digit(num):
    n = num

    while n > 0:
        ldigit = n % 10
        print(ldigit)
        n = n // 10

print(last_digit(5873))