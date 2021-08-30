def gridTravelerOptimize(n,m, dict ={}):
    key = str(n) + "," + str(m)
    if key in dict:
        return dict[key]
    if n == 0 or m == 0:  # if either row or column is 0, we can't move
        return 0
    if n == 1 and m == 1:  # if both row or column are 1, only 1 possible path
        return 1
    dict[key] = gridTravelerOptimize(n-1,m, dict) + gridTravelerOptimize(n,m-1, dict)
    return dict[key]

print(gridTravelerOptimize(3,7))