def longest_substring_with_k_distinct(str1, k):
    longest_sub = ""
    win_start,win_end = 0,0
    map = dict()

  #hashmap to keep track of the letters in the string
    for i, letter in enumerate(str1):
        if letter not in map:
            map[letter] = 1
        else:
            if map[letter] >= k:
                break
            else:
                map[letter] += 1
        win_end += 1
        longest_sub += letter

    longest_sub = win_end - win_start
    curr_subb = win_end - win_start
    win_end += 1
    while win_start <= win_end:
        if map[win_end] > k:
            while(map[win_end] > k):
                map[win_start] -= 1
                win_start += 1
        elif win_end < len(str1):
            win_end += 1



  #   longest_sub = str1[win_start:win_end]
  #   curr_sub = str1[win_start:win_end]
  #   longest_size = len(longest_sub)
  #
  #   #while win_start <= win_end:
  #
  #   #check if next letter(win_end) has a value greater than s>
  #   #if so, while win(end) value > greater than s, move win_start
  #
  #   #else
  #   #increment win_end
  #
  #   # longest_size = max(len(longest_sub), win_end-win_start)



    return 0


(longest_substring_with_k_distinct("araaci", 2))