def freq_get(nums):
    freq = {}
    n = len(nums)
    for i in range(n):
        freq[nums[i]] = freq.get(nums[i], 0) + 1
    return freq

print(freq_get([1,1,1,2,2,2,2,4,5,5,6,6,6]))
