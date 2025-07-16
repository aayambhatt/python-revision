def frequency_map(nums):
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums]=1
    return freq