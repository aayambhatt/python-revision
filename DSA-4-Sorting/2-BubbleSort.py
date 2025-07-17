def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):  # Go up to the unsorted part
            if nums[j] > nums[j + 1]:  # If current > next, swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

