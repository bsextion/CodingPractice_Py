#if either row or column is 0, return 0
#if row and column is both 1, return 1

def gridTraveler(n,m):
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return n
    return gridTraveler(n-1,m) + gridTraveler(n,m-1)

print(gridTraveler(2,3))
