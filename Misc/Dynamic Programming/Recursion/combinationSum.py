class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        combinations(candidates, target, result, [])
        return result

def combinations(nums, target, result, currArr):

    if sum(currArr) == target:
        if currArr not in result:
            result.append(currArr)
        return
    if sum(currArr) > target:
        return

    for num in nums:
        temp = currArr + [num]

        combinations(nums, target, result, sorted(temp))
# def combinations(j, nums, target, result, currArr ):
#
#     if sum(currArr) == target:
#         result.append(currArr)
#         return
#     if sum(currArr) > target:
#         return
#
#     for i in range(j, len(nums)):
#         temp = currArr + [nums[i]]
#         combinations(i,nums, target, result, temp)

soliution = Solution
soliution.combinationSum("",[1, 2, 3, 4, 5
                             ], 5)
