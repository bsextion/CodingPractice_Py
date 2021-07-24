from collections import deque

def isMatch(p1, p2):
        if p1 == "{" and p2 == "}":
            return True
        elif p1 == "[" and p2 == "]":
            return True    
        elif p1 == "(" and p2 == ")":
            return True
        else:
            return False
        
class Solution:
    def isValid(self, s: str) -> bool:
        map = {"{":"}", "(":")", "[":"]"}
        stack = deque() 
        for letter in s:
            if letter in "{([":
                stack.append(letter)
            elif not len(stack) == 0:
                popped = stack.pop()
                if(not isMatch(popped, letter)):
                    return False
            else: 
                return False            
        return len(stack) == 0                
           