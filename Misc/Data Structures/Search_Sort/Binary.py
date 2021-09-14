
#leftpointer and rightpointer and midpoint
#while leftpointer <= rightpointer
#calulcate midpointer = left + right/2
#if mid == target, return midpoint
#if arr[mid] < target, move the leftpointer = midpoint +1
#else, move the right pointer midpont-1

#return
def binarySearch(array, target):
    left_pointer, right_pointer = 0,len(array)-1
    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer)//2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left_pointer = mid +1
        else:
            right_pointer = mid-1
    return -1

print(binarySearch([1,4,5,6,9,15], 4))


