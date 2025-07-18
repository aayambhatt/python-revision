from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        j = i+1

        while j < len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j] = nums[j], nums[i]

            j+=1
        
        return i+1
        