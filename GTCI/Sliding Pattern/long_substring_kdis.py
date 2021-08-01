#**Problem**#
#Given a string, find the length of the longest substring in it with no more than K distinct characters

#1 Create empty map,longest_sub
#2 starting from the first char:
#3 if value appears in map already, increment count in map
#4 if value does not appear, check if len of map already k, if so end loop, else add lette to map
#5 reset dict, distinct count, and update start
#6 continue until we looped through all possible characters

def longest_substring_with_k_distinct(str1, k):
  map = dict()
  longest_sub = 0
  dist_count = 0
         
  for i in range(0, len(str1)):
      for j in range(i, len(str1)):
          letter = str1[j]
          if str1[j] in map:
              map[letter] +=1
              dist_count += 1   
          else:
              if len(map) == k:
                  longest_sub = max(longest_sub, dist_count)
                  break 
              else:
                  map[letter] = 1
                  dist_count += 1  
      map.clear()
      dist_count  = 0
  return longest_sub

longest_substring_with_k_distinct("araaci", 2)    
                  
                