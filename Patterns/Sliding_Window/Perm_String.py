def find_permutation(word:str, pattern):
  #get size of pattern
  size = len(pattern)
  win_start = 0
  win_end = size
  pattern = sorted(pattern)


  while win_end <= len(word):
    temp = sorted(word[win_start:win_end])
    if temp == pattern:
        return True
    win_start += 1
    win_end += 1


  return False

find_permutation("aaacb", "abc")