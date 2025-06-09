# has two functions, merge and merge_sort
# at the lowest level of this, the two sorted lists will only have one element each

#merge_sort pseudocode
# 1. if the length of the array A is already less than two, its is already sorted, so return it
# 2. split the array into two halves down the middle 
# 3. call merge sort twice on each of the algorithms
# 4. return the result of calling of the merge sort 
#       merge(sorted_left_side , sorted_right_side) on the result of the merge_sort() calls

def merge_sort(nums):
    if len(nums) < 2 :
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

#merge pseudocode
# 1. create new final list of intergers
# 2. set i and j = 0. They will be used to keep track of the indices of the input lists - A and B
# 3. use a looop to iterate over A and B at the same time, compare the elements of A and B if 
#   the elemento of A is less than or equal to the elelment of B, add it to the final list
#   and increment i, otherwise, add the item in B to the final list and increment j
# 4. If there are any leftover items, then add them to the final list and return final list


def merge(left, right):
    result = []
    i,j = 0
    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
            continue
        # we can also say else instead of continue, it will be the same thing
        result.append(right[j])
        j = j+1

        # if any eleemnts are left :
        while i < len(left):
            result.append(left[i])
            i = i+1
        while j < len(right):
            result.append(right[j])
            j = j+1


# time compleixyt = O(nlogn)
# but pretty bad space complexity
