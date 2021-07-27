#if value at position i is in a,e,i,o,u, increment count

def iterative_count_consonants(input_str):
    vowels = "aeiou"
    count = 0
    for letter in input_str:
        if not letter.lower() in vowels and letter.isalpha():
            count += 1
    return count        
        
        
def recusrive_count_consonants(input_str, count = 0, idx=0):
    vowels = "aeiou"
    if idx == (len(input_str))-1:
        return count
    if not input_str[idx].lower() in vowels and input_str[idx].isalpha():
        count += 1
    return recusrive_count_consonants(input_str, count, idx+1)  
               
print(recusrive_count_consonants("Welcome to Educative!"))            
