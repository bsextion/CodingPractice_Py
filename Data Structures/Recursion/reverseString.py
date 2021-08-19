def reverseString(s, i=0):
    if len(s) == i:
        return

    reverseString(s, i+1)
    print(s[i])

reverseString("cat")
