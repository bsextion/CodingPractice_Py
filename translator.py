def translate(phrase):
    translation = ""
    num = 3
    for letter in phrase:
        if letter in "AEOIUaseiou":
            translation += "g"
        else:
            translation += letter
    return translation.capitalize();        
                
        
        
print(translate("zebra"))
