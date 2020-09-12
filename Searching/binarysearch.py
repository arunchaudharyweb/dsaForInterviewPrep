def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1
    return -1