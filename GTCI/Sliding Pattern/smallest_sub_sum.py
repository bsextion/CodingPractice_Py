#**Problem**#
#Given an array of positive numbers and a positive number ‘S,’ 
#Find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S


#Solution 1
#1)Check if S exists, if it exists, return immeditaly in array
#2) Starting with size n, check all possible subarrays equal to S
#3) If S isn't found, increase the scope of subarray size and do loop again
#4) Continue until subarray size is greaer than original array size
#5) Repeat 2-4 S until S is found or subarray size is greaer than original array size
#6) Return 0 if S was never found
def smallest_subarray_with_given_sum_s1(s, arr):
    subarr = []
    winStart = 0
    max_len = 1
    winEnd = max_len
    
    while max_len <= len(arr):
        subarr = arr[winStart:winEnd]   
        while winEnd <= len(arr):
            if sum(subarr) >= s:
                return max_len
            winStart += 1
            winEnd += 1
            subarr = arr[winStart:winEnd]  
            
        max_len += 1
        winStart = 0
        winEnd = max_len
            
          
    return 0

smallest_subarray_with_given_sum_s1(7, [2, 1, 5, 2, 3, 2])