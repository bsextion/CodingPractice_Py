class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        result = []
        getChange(amount, coins, [], result)
        if len(result) == 0:
            return -1
        return len(result[0])


def getChange(target, coins, current, result):
    if len(result) > 0:
        return result
    if sum(current) == target:
        result.append(current)
        return
    if sum(current) > target:
        return
    for coin in coins:
        temp = current + [coin]
        getChange(target, coins, temp, result)

Solution.coinChange("", [186,419,83,408], 6249)