def merge(left_arr, right_arr, result):
    lft_ptr, rgt_ptr, res_ptr = 0, 0, 0

    while lft_ptr < len(left_arr) and rgt_ptr < len(right_arr):
        if left_arr[lft_ptr] < right_arr[rgt_ptr]:
            result[res_ptr] = left_arr[lft_ptr]
            lft_ptr += 1
            res_ptr += 1
        else:
            result[res_ptr] = right_arr[rgt_ptr]
            rgt_ptr += 1
            res_ptr += 1

    while (lft_ptr < len(left_arr)):
        result[res_ptr] = left_arr[lft_ptr]
        lft_ptr += 1
        res_ptr += 1

    while (rgt_ptr < len(right_arr)):
        result[res_ptr] = right_arr[rgt_ptr]
        rgt_ptr += 1
        res_ptr += 1

    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    midpoint = len(lst) // 2
    left_arr = lst[:midpoint]
    right_arr = lst[midpoint:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    return merge(left_arr, right_arr, lst)


print(merge_sort([1,8,9,2,3]))