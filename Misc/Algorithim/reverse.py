class Solution:
    def reverse(self, x: int) -> int:
        num = x
        if x < 0:
            isNegative = True
            num = abs(x)
        wordNum = str(num)
        num = int(wordNum[::-1]) 
        
        if isNegative:
               num *= -1
        if num <= pow(2, -31) or num >= pow(2,31)-1:
            return 0
        return num
    
    
    reverse("", -123)       