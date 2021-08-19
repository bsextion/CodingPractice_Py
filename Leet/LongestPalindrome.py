class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        result.append(s[0])
        if len(s) <= 1:
            return s[0]


        if len(s) > 1 and s[0] == s[1]:
            result.append(s[0:2])

        for i in range(1, len(s)):
            checkPalindrome(s, result, i, i + 1)  # odd number
            checkPalindrome(s, result, i, i + 2)  # even number
        result.sort(key=len)
        return result[-1]

def checkPalindrome(word, result, start, end):
    while start >= 0 and end <= len(word):
        palindrome = word[start:end]
        if palindrome == palindrome[::-1]:
            result.append(palindrome)
            start -= 1
            end += 1
        else:
            break

Solution.longestPalindrome("","bb")