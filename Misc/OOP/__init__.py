from collections import Counter
def find_single_number(arr):
  num = 0
  for i in arr:
      num ^= i
  return num

find_single_number([1, 4, 2, 1, 3, 2, 3])