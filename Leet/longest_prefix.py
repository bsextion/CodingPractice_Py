class Solution(object):
    #sort the list from shortest to longest
    #get the first word, this will be a base case for every other word
    #for each letter in word
    #for each subletter in subword
    #if letter and subletter are not equal
    #return word[0:i-1]
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        
        word = "" if len(strs) <= 0 else strs[0]
        for index, letter in enumerate(word):
            for n, subword in enumerate(strs[1::], start = 1):
                if letter != subword[index]:
                    return word[:index]
            
        return word    
            
        """
        :type strs: List[str]
        :rtype: str
        """
    print(longestCommonPrefix("", ["dog","racecar","car"]))      