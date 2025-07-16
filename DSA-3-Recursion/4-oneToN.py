def print_numbers(n):
    if n == 0:
        return  # base case: stop when n is 0
    print_numbers(n - 1)  # recursive call with n-1
    print(n)  # print after recursive call to go from 1 to N

# Example:
print_numbers(5)
