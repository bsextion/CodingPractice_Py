# two pointers, next, nonNo
# map to hold values

# for each num in array
# if num is not in map, increment pointers, pass value into next non Dup
# if num is in map, increment next pointer
def removeDuplicates(self, nums):
    next, next_nonDup = 0,0


    for num in nums:
        num_exist = num in map.keys()
        if num_exist is False:
            map[num] = 1
            nums[next_nonDup] = num
            next_nonDup += 1

        next += 1

    return next_nonDup

removeDuplicates("", [1,1,2])