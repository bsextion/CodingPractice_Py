#**Problem**#
#Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.


#Solution 1
#1) create left pointer pointer to first el, right pointer pointing to last el
#2) loop through array and check if sum of left and right pointers equal target
#3) if sum equals target, return positions
#4) else sum not equal to target, if sum is too high, move the right pointer and recalculatte. if sum too low, move the left pointer and recaluclate
#5)continue until pair is found or left pointer passes right pointer

def pair_with_targetsum(arr, target_sum):
  left_pointer, right_pointer = 0, len(arr)-1
  
  while(left_pointer < right_pointer):
      actual_sum = arr[left_pointer] + arr[right_pointer]
      if actual_sum == target_sum:
          return [left_pointer, right_pointer]
      elif actual_sum > target_sum:
          right_pointer -= 1
      else:
          left_pointer += 1    
          
  return [-1, -1]

pair_with_targetsum([1, 2, 3, 4, 6], 6)