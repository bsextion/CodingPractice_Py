
    # i = 0
    #result arr
  #while i < less than len(s)
  #count = 0
  #while i < less than len(s) and s[i] and s[i+1]

  #result append count and s[i]
  #joim

def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

next_number("21", 5)







next_number("21")