def find_minimum(nums):
    if len(nums == 0):
        return None

    min = float("inf")
    #initalizes the starting point as +ve infinity, since we are going to find the 
    # minimum element, starting point can be the maximum element we can 
    for num in nums :
        if num < min:
            min = num
        return min

 

