def backspace_compare(str1:str, str2):
    #two pointers,
    ptr_one = 0
    ptr_two = 0

    while ptr_one < len(str1):
        if str1[ptr_one] is '#' and ptr_one > 0:
            temp = list(str1)
            temp[ptr_one-1] = ''
            temp[ptr_one] = ''
            str1 = ''.join(temp)
        ptr_one += 1

    while ptr_two < len(str2):
        if str2[ptr_two] is '#' and ptr_two > 0:
            temp = list(str2)
            temp[ptr_two - 1] = ''
            temp[ptr_two] = ''
            str2 = ''.join(temp)
        ptr_two += 1

    if str1 == str2:
        return True
    return False

backspace_compare("xp#", "xyz##")
