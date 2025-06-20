class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")  # This means the lowest number possible

        for i in range(len(nums)):
            curr_sum += nums[i]         # Add the current number to curr_sum
            max_sum = max(max_sum, curr_sum)  # Update max_sum if curr_sum is bigger

            if curr_sum < 0:            # If curr_sum goes below 0, reset it to 0
                curr_sum = 0
        
        return max_sum
