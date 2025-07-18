def slargest(nums):
    largest = float('-inf')
    seclargest = float('-inf')

    for num in nums:
        if num > largest:
            largest = num
    
    for num in nums:
        if num > seclargest and num!=largest:
            seclargest = num
    
    return seclargest


print(slargest([1,2,3,4,5,6,7,8,9]))