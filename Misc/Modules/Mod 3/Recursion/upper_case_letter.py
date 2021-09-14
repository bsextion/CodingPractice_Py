def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
                return input_str[i]
    return "No uppercase character found"

def find_uppercase_recursion(input_str, i=0):
    if i == len(input_str)-1:
      return "No uppercase character found"
    else:
        if input_str[i].isupper():
            return  input_str[i]
        find_uppercase_recursion(input_str, i+1) 

  
print(find_uppercase_recursion("LucidProgramming"))