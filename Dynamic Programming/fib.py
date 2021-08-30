#Time: O(2n)
def fib(n, memo={}):
  if n in memo: return memo[n]
  if n <= 1: return n  #base case 1

  memo[n] = fib(n-1, memo) + fib(n-2, memo)
  return memo[n]

print(fib(8))