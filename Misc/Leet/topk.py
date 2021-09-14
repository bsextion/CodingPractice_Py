from collections import Counter
class Solution:
    def topKFrequent(self, nums: [], k: int) -> []:
        return dict(Counter(nums).most_common(k)).keys()



        # result = []
        # map = dict()
        # # if size 1, return value at nums[0]
        # if len(nums) == 1:
        #     result.append(nums[0])
        #
        # for num in nums:
        #     if num in map:
        #         map[num] += 1
        #     else:
        #         map[num] = 1
        #
        # map = sorted(map,key=map.get,reverse=True)
        #
        # for i, key in enumerate(map):
        #     if i == k:
        #         break
        #     result.append(key)
        # return result


Solution.topKFrequent("", [3,0,1,0], 2)