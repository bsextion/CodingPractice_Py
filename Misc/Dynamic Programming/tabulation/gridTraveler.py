def gridTravel(m,n):
    table = [[0 for c in range(0,m+1)]for r in range (0, n+1)]
    table[1][1] = 1

    for i in range(0, m+1):
        for j in range(0, n+1):
            current = table[i][j]
            if j +1 <= n: table[i][j+1] += current
            if i+1 <= m: table[i+1][j] += current
    return table[m][n]





print(gridTravel(3,3))