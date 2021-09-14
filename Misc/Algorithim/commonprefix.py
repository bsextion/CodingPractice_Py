from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        word = strs.pop(0)
        isFound = False

        while not isFound and not len(word) == 0:
            for string in strs:
                if not string.startswith(word):
                    word = word[:-1]
                    isFound = False
                    break
            else:
                isFound = True    
        return word        

                
     
        ##sort by length, get the first word
        ##loop through each word to determine if word is in words[x]
        ##if not in word, break the loop and remove the last word
        
        
    longestCommonPrefix("", ["dog","racecar","car"]
)   