
def smallest_subarray_with_given_sum(s, arr):
    # while sum of window is less than 0, increase the size
    win_start, win_end,curr_size = 0 ,0, len(arr)
    while sum(arr[win_start:win_end]) < s:
        win_end += 1

    smallest_size = len(arr[win_start:win_end])

    # once we have the intial size from the beginning, store as smallest size
    while win_start <= win_end:
        curr_win = arr[win_start:win_end]
        if sum(curr_win) < s and win_end < len(arr):
            win_end += 1
        else:
            win_start += 1

        if sum(arr[win_start:win_end]) >= s:
            curr_size = len(arr[win_start:win_end])
        smallest_size = min(curr_size, smallest_size)
    return smallest_size


print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))


