
def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remain = targetSum - num
        if canSum(remain, numbers, memo) == True:
            memo[targetSum] = True
            return True
    return False

print(canSum(7, [2,3]))


