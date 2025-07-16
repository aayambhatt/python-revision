def count_digits(num):
    n = abs(num)
    count = 0

    if n == 0:
        return 1

    while n > 0:
        count += 1
        n = n // 10

    return count

print(count_digits(0))      # 1
print(count_digits(1655))   # 4
print(count_digits(-1234))  # 4
