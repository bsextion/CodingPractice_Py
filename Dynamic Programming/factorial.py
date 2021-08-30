def factorial(n, map):
    if n <= 1:
        return 1
    elif n in map:
        return map[n]

    map[n] = n * factorial(n-1, map)
    return map[n]

print(factorial(5, {}))