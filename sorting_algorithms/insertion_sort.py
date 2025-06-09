# typically used for mostly sorted lists
# even though O(n^2) for this on largers lists
# its actually faster than merge sort in smaller lists

# pseudocode for insertion sort 
"""
1. set j variable to the current index
2. while j is greater than 0, and the element at j-1 is greater than element at j:
    1. swap j and j-1 
    2. decreement j by 1
3. return the list
"""

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            #swapping 
            nums[j] , nums[j-1] = nums[j-1] , nums[j]
            j -= 1
    return nums
