def remove_duplicates(nums):
    seen = set()
    k = 0
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[k] = nums[i]
            k += 1
    return k
