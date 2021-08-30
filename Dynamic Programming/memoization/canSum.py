
def canSum(targetSum, numbers):
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        remain = targetSum - num
        if canSum(remain, numbers) == True:
            return True
    return False

print(canSum(7, [2,3]))