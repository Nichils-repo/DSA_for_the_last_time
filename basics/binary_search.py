# starts with a sorted array
# go in halves


def binary_search(target,arr):

    low = 0
    high = len(arr) - 1

    while low<=high:
        med = (low+high) // 2
        if arr[med]  == target:
            return True
        if arr[med] <target:
            low = med +1 
            continue 
        high = mid - 1
    return False
