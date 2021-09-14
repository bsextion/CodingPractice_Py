# def get_permutations(word):
#     result = []
#     permute(word,result, "", word)
#     return result
#
# def permute(word, result, currWord, remaining):
#
#     if remaining == "":
#         result.append(currWord)
#         return
#
#     if len(currWord) == len(word):
#         return
#
#     for letter in word:
#         temp = currWord + letter
#         permute( word, result, temp, remaining.replace(letter, "", 1))
#
# get_permutations("abc")
#
#

class Solution(object):
    def permute(self, nums):
        result = []
        getPermuations(nums, result, [])
        return result

def getPermuations(nums, result, current):
    if len(current) == len(nums) and sorted(nums) == sorted(current):
        if current not in result:
            result.append(current)
        return
    if len (current) >= len(nums):
        return

    for num in nums:
        temp = current + [num]

        getPermuations(nums,result, temp)

Solution.permute("", [1,1,2])