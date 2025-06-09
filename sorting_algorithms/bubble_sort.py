def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        # if the algo does not even swap once during the entire pass, then the array is already sorted
        for i in range(1,end):
            if nums[i-1] > nums[i]:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i]  = temp
                swapping = True
            
        end -= 1

