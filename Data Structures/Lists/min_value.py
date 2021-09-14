#merge sort
def find_minimum(arr):
    result = merge_sort(arr)
    return result[-1]


def merge_sort(arr):
    # if len(arr) <= 0
    if len(arr) <= 1:
        return

    # create left, right arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # call mergesort on both sides
    merge_sort(left_arr)
    merge_sort(right_arr)

    # merge back together
    sorted_arr = merge(left_arr,right_arr, arr)

    # Write your code here
    return sorted_arr

def merge(left_arr, right_arr, result):

    lft_ptr,rgt_ptr,rst_ptr = 0, 0, 0

    while lft_ptr < len(left_arr) and rgt_ptr < len(right_arr):
        if left_arr[lft_ptr] < right_arr[rgt_ptr]:
            result[rst_ptr] = left_arr[lft_ptr]
            lft_ptr += 1
            rst_ptr += 1
        else:
            result[rst_ptr] = right_arr[rgt_ptr]
            rgt_ptr += 1
            rst_ptr += 1

    while lft_ptr < len(left_arr):
        result[rst_ptr] = left_arr[lft_ptr]
        lft_ptr += 1
        rst_ptr += 1

    while rgt_ptr < len(right_arr):
        result[rst_ptr] = right_arr[rgt_ptr]
        rgt_ptr += 1
        rst_ptr += 1

    return result


find_minimum([9,2,3,6])

