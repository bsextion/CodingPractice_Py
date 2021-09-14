
# store the first k-2 elements in small list
# extend the original list by the small list
#remove the k-2 from original list
def right_rotate(lst, k):
    size = k
    result = lst[::-1][:k][::-1]

    lst = lst[::-1][k:][::-1]
    result.extend(lst)
    return result

right_rotate([0, 0, 0, 2], 2)

# remove the last k elements and store in list