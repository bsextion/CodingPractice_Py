#**Problem**#
#Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
#1)Sort the array
#2)left and right pointer
#3) In a foor loop, i < len(-2)
#4) while loop, left is less than right
#5) if triplet equal 0, add to array
#6) outside of while loop, set left to i and left to last

def search_triplets(arr):  
  triplets = []
  arr = sorted(arr)
  for index, value in enumerate(arr):
      if index == len(arr)-2:
          break
      left_ptr, right_ptr = index+1,len(arr)-1
      while(left_ptr < right_ptr):
          cur_arr= [value, arr[left_ptr], arr[right_ptr]]
          cur_sum = sum(cur_arr)
          if cur_sum == 0:
              if not cur_arr in triplets:
                  triplets.append([value, arr[left_ptr], arr[right_ptr]])
              right_ptr -= 1
              left_ptr += 1      
              
          elif cur_sum > 0:
              right_ptr -= 1
          else:
              left_ptr += 1      
          
  # TODO: Write your code here
  return triplets

search_triplets([-3, 0, 1, 2, -1, 1, -2])