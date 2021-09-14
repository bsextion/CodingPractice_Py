
def howSum(n, arr):
    result, length = [], n+1
    table = [0] * length
    table[0] = []
    for i in range(0, n):
        if table[i] != 0:
            for num in arr:
                if i + num <= n:
                    table[i+num] = [x for x in table[i]]
                    table[i+num].append(num)
                if i + num == n and sorted(table[i+num]) not in result:
                    result.append(table[i+num])




    return table[n]


howSum(7, [5,3,4])