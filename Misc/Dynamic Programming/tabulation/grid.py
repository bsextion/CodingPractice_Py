
def grid(m,n):
    row,col = m+1,n+1
    table = [[0 for c in range(0,col)]for r in range (0, row)]
    table[1][1] = 1

    for r in range(0, m+1):
        for c in range(0, n+1):
            curr = table[r][c]
            if c+1 <= n: table[r][c+1] += curr
            if r +1 <= m: table[r+1][c] += curr
    return table[m][n]
print(grid(2,3))
