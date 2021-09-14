def howSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainresult = howSum(remainder, numbers)
        if remainresult is not None:
            memo[targetSum] = [*remainresult, num]
            return memo[targetSum]
    return None


print(howSum(7, [2,3]))
