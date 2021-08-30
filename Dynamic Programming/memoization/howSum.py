def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainresult = howSum(remainder, numbers)
        if remainresult is not None:
            return [*remainresult, num]
    return None


print(howSum(7, [2,3]))
