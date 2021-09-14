def max_sub_array_of_size_k(k, arr):
    win_end,win_start = k,0
    max_sum = sum(arr[0:k])
    curr_sum = sum(arr[0:k])

    while win_end <= len(arr)-1:
        curr_sum -= arr[win_start]
        curr_sum += arr[win_end]
        max_sum = max(curr_sum, max_sum)
        win_start += 1
        win_end += 1
    return max_sum



print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))