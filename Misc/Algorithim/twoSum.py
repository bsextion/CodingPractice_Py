from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index in range(len(nums)):
            numberNeeded = target - nums[index]
            if map.get(numberNeeded, False) is not(False):
                return [map.get(numberNeeded), index]
            else:
                map[nums[index]] = index
       
    twoSum("", [2,7,11,15], 9)            
        
            
            
        