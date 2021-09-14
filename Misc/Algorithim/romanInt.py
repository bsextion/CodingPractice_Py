class Solution(object):
    def romanToInt(self, s):
        #create map
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        number = 0
        while(not i == len(s) ):
            if s[i] == "I" and not i+1 == len(s) and  s[i+1] in "VX":
                number += (map.get(s[i+1]) - map.get(s[i]))
                i += 2
            elif s[i] == "X" and not i+1 == len(s) and  s[i+1] in "LC":
                number += (map.get(s[i+1]) - map.get(s[i]))
                i += 2
            elif s[i] == "C" and not i+1 == len(s) and  s[i+1] in "DM":
                number += (map.get(s[i+1]) - map.get(s[i]))
                i += 2
            else:
                number += (map.get(s[i]))
                i += 1
        return number        
        
    romanToInt("", "LVIII")        