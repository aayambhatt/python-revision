def maxi(nums):
    max_so_far = float('-inf')

    for num in nums:
        if num > max_so_far:
            max_so_far = num
    
    return max_so_far

print(maxi([99,2,5,67,4,2,1,132,56,100]))