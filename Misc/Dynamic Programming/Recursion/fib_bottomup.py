fib = {}
def fibsequence(n):
    if n <= 1:
        return n
    if n in fib:
        return fib[n]

    fib[n] = fibsequence(n-1) + fibsequence(n-2)
    return fib[n]


print(fibsequence(6))