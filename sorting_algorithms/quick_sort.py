"""
pesudo code for quick sorting 
1. provide a pivot element - arbitrarily the last one here 
2. start i at -1 and j at 0, and set pivot
3. if element at j>pivot, then update j to j+1, no other changes
4. if element at j < pivot, then swap elements at j and i, update j to j+1 and i to i+1
5. until j reaches top end of list, excluding pivot.
6. now all the numbers less than the pivot are on the left and all the number greater
    than the pivot are on the right 
7. move the pivot to its correct appropriate position
8. recursively repeat for both section
"""
"""
the process is started for quicksort(array, 0, len(array)-1) cuz we are taking the last element
as the pivot 
"""

def quick_sort(nums,high,low):
    if low<high:
        p = partition(nums,low,high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p+1, high)


def partition(nums, high,low):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot :
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i] , nums[high] = nums[high], nums[i]
    return i

