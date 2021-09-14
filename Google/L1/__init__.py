class Solution(object):
    def sumZero(self, n):
        arr = [x for x in range(1, int(n/2)+1)]
        arr.extend(list(map(lambda x: x * -1, arr)))

        if n % 2 != 0: arr.append(0)
        return arr

Solution.sumZero("", 5)