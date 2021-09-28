def kadanesAlgorithm(array):
    start, end = 0, 1
    max_sum = array[start]

    while end < len(array):
        curr_sum = sum(array[start:end])
        if sum(array[start:end]) + array[end] < array[end]:
            curr_sum = array[end]
            start = end
            end = end +1

        else:
            curr_sum += array[end]
            end += 1

        max_sum = max(curr_sum, max_sum)
    return max_sum

kadanesAlgorithm([1, 2, -4, 3, 5, -9, 8, 1, 2])