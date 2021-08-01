#**Problem**#
#Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
#1)Create two pointer, nonDup, next
#2) loop over array while next is less than len
#)3 if number is not duplicate, move both pointers
#4) if number is duplicate, move next pointer
#5) if not dup, put number at next position in the last non dup pointer, if dup, move next


def remove_duplicates(arr):
  non_dup_ptr, next_potr = 1, 1
  while(next_potr < len(arr)):
      if arr[next_potr] != arr[next_potr-1]: 
              arr[non_dup_ptr] = arr[next_potr]
              non_dup_ptr += 1
          
      next_potr += 1
  return len(arr[0:non_dup_ptr]) 
        
                  
remove_duplicates([2, 2, 2, 11])              