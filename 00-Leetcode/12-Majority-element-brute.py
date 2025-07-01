from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        maj_element = -1
        for key, value in freq.items():
            if value>(n/2):
                maj_element = key
        
        return maj_element

        