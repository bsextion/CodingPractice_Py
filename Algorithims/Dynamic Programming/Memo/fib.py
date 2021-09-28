def fib(n, map):
    if n in map:
        return map[n]

    if n <= 1:
        return n

    map[n] = fib(n-1, map) + fib(n-2, map)
    return map[n]

fib(5, {})