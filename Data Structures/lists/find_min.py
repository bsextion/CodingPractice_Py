def find_minimum(arr):
    smallest = arr[0]

    for i in range(1, len(arr)):
        smallest = min(smallest, arr[i])

    return smallest