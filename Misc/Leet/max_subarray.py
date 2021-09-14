#curr_max
#max_result
#contigius array
#outer loop starting at first position (x)
#in the inner loop, we will grab x numbers and get sum
#if curr_max is larger than max_result, store in max result and grab continours arr
#slide the window by subtracting the previous and adding the next

#return the max result

class Solution(object):
    def maxSubArray(self, nums):
        curr_max, max_result = 0,0
        max_array = []

        for x in range(0, len(nums)):
            cur_range = x+1
            curr_arr = nums[0:cur_range]
            curr_max = sum(curr_arr)

            if curr_max > max_result:
                max_array = curr_arr
                max_result = curr_max

            if cur_range == len(nums):
                break
            for i in range(1, len(nums)):
                curr_max -= nums[i-1]
                curr_max += nums[i]
                if curr_max > max_result:
                    max_result = curr_max
                    max_array = nums[i:i+cur_range]

        return max_array








    print(maxSubArray("", [-2,1,-3,4,-1,2,1,-5,4]))