def permutation(phrase, phrase2):
    phrase = phrase.lower()
    phrase2 = phrase2.lower()
    map = dict()
    
    for letter in phrase:  #store count from first word in map
        if letter in map:
            map[letter] += 1 
        else:
            map[letter] = 1
    
    
    for letter in phrase2:  #remove count based on letters in second word
        if letter in map:
            map[letter] -= 1 
        else:  #letter didn't appear then an extra letter has shown up
            return False
        
    return all(value == 0 for value in map.values()) #returns true if condition is met for all values   


print(permutation("google", "ooggle"))

