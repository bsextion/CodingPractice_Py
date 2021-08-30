class Solution:
    def lengthOfLongestSubstring(self, s:str):
        start,end = 0,1
        map, result_arr = dict(),[s[0]]
        temp = s[0]
        map[temp] = 1

        while(end < len(s)):
            letter = s[end]
            if not letter in map:
                map[letter] = 1
                temp = s[start:end+1]
                result_arr.append(temp)
            #if letter not in map, add to map, increase the temp and add to reuslt arr

            else:
                map.clear()
                start += 1
                end = start + 1
                map[s[start]] = 1
                temp = s[start:end]
                result_arr.append(temp)

            #if letter in map, clear map, move start by 1, reset end to start, add to arr
            end += 1






print(Solution.lengthOfLongestSubstring("", "abcadf"))
