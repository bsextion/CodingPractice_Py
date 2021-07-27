def permutation(phrase):
    phrase = phrase.replace(" ", "")
    phrase = phrase.lower()
    map = dict()
    for letter in phrase: #map to keep track of how many times a letter appears
        if letter in map:
            map[letter] += 1 
        else:
            map[letter] = 1
    
    isEven = True if len(phrase) % 2 == 0 else False
    oddNumber = 0
    
    for key in map.keys(): #if even len string, all characters will appear an even amount of times
        if map[key] % 2 != 0: #if odd len string, only one character will appear once, every other character appears an even amount
            oddNumber += 1
    
    if isEven:
        return oddNumber == 0
    
    else:
        return oddNumber == 1
    
           
                    

print(permutation("tacocat"))