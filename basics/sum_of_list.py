def sum(nums):

    s = 0
    if len(nums) == 0:
        return 0
    
    for n in nums:
        s = s + n

    return s

