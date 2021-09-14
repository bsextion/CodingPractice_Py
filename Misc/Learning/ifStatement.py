# isMale = True
# isTall = True

# if isMale and isTall:
#     print("You are a male")
# elif isMale and not(isTall):
#     print("")    
# else:
#     print("You are not a male")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))        

