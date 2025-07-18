def arraySorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False  
    return True  

print(arraySorted([1,2,3,4,5]))  
print(arraySorted([1,2,3,2,7]))  
