#**Problem**#
#Given an array of positive numbers and a positive number ‘k,’find the max sum of any contiguous subarray of size ‘k’.


#Solution 1
#1) For size k, get the first k elements in array
#2) Calculate sum of the array
#3) Compare current sum to the largest sum stored
#4) Repeat until K is out of bounds in the array
def max_sub_array_of_size_k_s1(k, arr):
  largest_sum, window_start = 0,0
  window_end = k
  
  while(window_end <= len(arr)):
      sub_array = arr[window_start:window_end]
      curr_sum = sum(sub_array)
      largest_sum = max(largest_sum, curr_sum)
      window_start += 1
      window_end += 1
  
  return largest_sum

#Solution 2
#1) For size k, get the first k elements in array
#2) Calculate the sum 
#3) Compare current sum to the largest sum stored
#4) remove first and add next value
#5) Repeat 1-4
#4) Continue until we cannot create more subarray of size k
def max_sub_array_of_size_k_s2(k, arr):
  largest_sum, window_start = 0,0
  window_end = k-1
  sub_array = arr[window_start:k]
  curr_sum = sum(sub_array)
  while(window_end < len(arr)-1):
      largest_sum = max(largest_sum, curr_sum)
      curr_sum-= arr[window_start]
      window_start += 1
      window_end += 1
      curr_sum += arr[window_end]
  largest_sum = max(largest_sum, curr_sum)
  return largest_sum


print(max_sub_array_of_size_k_s2(2, [2, 3, 4, 1, 5]))

