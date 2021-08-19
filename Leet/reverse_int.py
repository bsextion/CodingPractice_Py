#Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], return 0.

#Sol 1: store in stack
#Sol 1: Math
from math import *
from collections import deque
import math
class Solution(object):
    def reverse_s1(self, x):
        result, result_str = 0, ""
        queue = deque()
        min_int = math.pow(-2, 31)
        max_int = (math.pow(2, 31))-1
        
        is_neg = True if x < 0 else False
        if is_neg:
            x *= -1
        
        for digit in str(x):
            queue.append(digit)
            
        length = len(queue)
        for _ in range(0, length):
            n = queue.pop()
            result_str += n
    
        result = int(result_str)    
        
        if is_neg:
            result = result * -1
    
        if result <= min_int or result >= max_int:
            return 0
        return result

    def reverse(self,x):
        result = 0
        min_int = math.pow(-2, 31)
        max_int = (math.pow(2, 31))-1
        
        while x > 0:
            remainder = x % 10
            x = x // 10
            result = (result * 10) + remainder
        
        if result <= min_int or result >= max_int:
            return 0
        return result
        
        
    print(reverse("", 123))