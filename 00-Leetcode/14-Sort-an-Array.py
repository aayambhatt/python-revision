class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Define the merge function inside
        def merge(arr1, arr2):
            merged = []
            i = j = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1

            while i < len(arr1):
                merged.append(arr1[i])
                i += 1

            while j < len(arr2):
                merged.append(arr2[j])
                j += 1

            return merged

        # Now define recursive merge_sort
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        # Start the merge sort on input nums
        return merge_sort(nums)
