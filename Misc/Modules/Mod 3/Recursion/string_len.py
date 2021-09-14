
def iterative_str_len(input_str):
    idx = 0
    while not input_str == '':
        input_str = input_str[:-1]
        idx += 1
    return idx

def recursion_str_len(input_str, idx=0):
    if idx == len(input_str):
        return idx
    return recursion_str_len(input_str, idx+1)
    
print(iterative_str_len("hello"))    
    