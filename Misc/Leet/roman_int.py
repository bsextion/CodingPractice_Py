# create map to hold all whole numbers
# loop though string
# if I and next is in "VX" subtract next - I, skip to the next next
# else add I and move to next
# do this for all numbers
class Solution(object):
    def romanToInt(self, s):
        result = 0
        i = 0
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i < len(s):
            curr_l = s[i]
            if i == len(s)-1:
                result += map[curr_l]
                break
            next_l = s[i+1]
            if curr_l is "I" and next_l in "VX":
                result += map[next_l] - map[curr_l]
                i += 2
                continue
            if curr_l == "X" and next_l in "LC":
                result += map[next_l] - map[curr_l]
                i += 2
                continue

            if curr_l == "C" and next_l in "DM":
                result += map[next_l] - map[curr_l]
                i += 2
                continue
            else:
                result += map[curr_l]
            i += 1
        return result

    print(romanToInt("", "IV"))


