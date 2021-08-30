memo = {}
def staircase(n, m):
    if n <= 1:
        memo[n] = 1
        return 1
    total = 0

    for x in range(1,m+1):
        if x <= n:
            total += staircase(n-x, m)
        memo[n] = total


    return memo[n]


print(staircase(4,3))