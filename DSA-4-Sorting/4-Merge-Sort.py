def merge(arr1, arr2):
    merged = []
    i, j = 0, 0
    n,m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    while i < n:
        merged.append(arr1[i])
        i+=1
    while j < m:
        merged.append(arr2[j])
        j+=1


    return merged
   

def merge_sort(arr):
    n = len(arr)

    # base case
    if n <= 1:
        return arr

    mid = n // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
    
    

# Example usage:
nums = [3,1,6,2,4,8,7]
sorted_nums = merge_sort(nums)
print(sorted_nums)
