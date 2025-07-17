def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if nums[j]<nums[minIndex]:
                minIndex = j
        nums[i],nums[minIndex] = nums[minIndex], nums[i]



arr = [5,4,3,2,1]
selectionSort(arr)
print(arr)
