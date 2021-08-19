def mergeSort(array):
    if len(array) <= 1:
        return array

    #split arr into left and right arr
    mid = len(array) //2
    left_array = array[:mid]
    right_array = array[mid:]
    mergeSort(left_array)
    mergeSort(right_array)

    #merge leftarr and right arr, and return arr
    arr = merge(left_array,right_array,array)
    return arr

def merge(left, right, arr):
    left_ptr, right_ptr, result_ptr = 0,0,0
    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] < right[right_ptr]:
            arr[result_ptr] = left[left_ptr]
            left_ptr += 1
        else:
            arr[result_ptr] = right[right_ptr]
            right_ptr += 1

        result_ptr += 1

    while left_ptr < len(left):
        arr[result_ptr] = left[left_ptr]
        left_ptr += 1
        result_ptr += 1

    while right_ptr < len(right):
        arr[result_ptr] = right[right_ptr]
        right_ptr += 1
        result_ptr += 1

    return arr


print(mergeSort([3,5,1,2,9,13,10]))

#while leftptr is less than left and rightptr less than right
#if left is less than right, add left to arr
#else add right to arr

#while loop to add remaining left

#while loop to add remaining right





