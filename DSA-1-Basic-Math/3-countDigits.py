def count_digits(num):
    string = str(num)
    count = 0

    for s in string:
        count+=1
    
    return count

print(count_digits(1655))