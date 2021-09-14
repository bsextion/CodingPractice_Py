
results = []
def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombo = None

    for num in numbers:
        remainder = targetSum - num
        remainderArr = bestSum(remainder, numbers)
        if remainderArr is not None:
            combination = [*remainderArr, num]
            if shortestCombo is None or len(combination) < len(shortestCombo):
                shortestCombo = combination
                results.append(combination)

    return res


print(bestSum(7, [3,4,7]))

