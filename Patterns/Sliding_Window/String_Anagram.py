import math
def find_product(lst):
    # Write your code here
    #for each list, remove pos i
    #multiply
    result = []

    for x in range(len(lst)):
        temp = lst.copy()
        temp.pop(x)
        result.append(multiply(temp))
    return result

def multiply(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print(find_product([1,2,3,4]))
