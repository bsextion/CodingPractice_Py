# result array to store length, set first value to 1
# counter starting at 1


# for loop starting at index 1
# if i-1 is less than i, increment counter and append to result
# else counter = 1, append to result

# sort list and return last value
class Solution:
    def lengthOfLIS(self, nums) -> int:
        result, counter = [1], 1

        for i in range(1, len(nums)+1):
            if nums[i-1] < nums[i]:
                counter += 1
            else:
                counter = 1

            result.append(counter)
        result.sort()
        return result[-1]

Solution.lengthOfLIS("",[10,9,2,5,3,7,101,18])










