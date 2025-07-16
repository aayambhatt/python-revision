def revArr(nums, left, right):
    if left >= right:
        return
    nums[left],nums[right] = nums[right], nums[left]
    return revArr(nums, left+1, right-1)

nums = [1, 2, 3, 4, 5]
revArr(nums, 0, len(nums) - 1)
print(nums)

