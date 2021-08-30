class Solution(object):
    def threeSum(self, nums):
        result = []
        temp_sum_arr = []

        nums.sort()
        for x in range(0, len(nums)-2):
            leftPointer = x+1
            rightPointer = len(nums)-1
            while leftPointer < rightPointer:
                temp_sum_arr = [nums[x], nums[leftPointer], nums[rightPointer]]
                if sum(temp_sum_arr) == 0:
                    if not temp_sum_arr in result:
                        result.append(temp_sum_arr)
                    leftPointer += 1
                    rightPointer -= 1
                elif sum(temp_sum_arr) < 0:
                    leftPointer += 1
                else:
                    rightPointer -= 1
        return temp_sum_arr

Solution.threeSum("", [-1,0,1,2,-1,-4])