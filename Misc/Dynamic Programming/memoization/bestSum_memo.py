
def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombo = None

    for num in numbers:
        remainder = targetSum - num
        remainderArr = bestSum(remainder, numbers)
        if remainderArr is not None:
            memo[targetSum] = [*remainderArr, num]
            combination = memo[targetSum]
            if shortestCombo is None or len(combination) < len(shortestCombo):
                shortestCombo = combination

    return shortestCombo


print(bestSum(7, [3,4,7]))

