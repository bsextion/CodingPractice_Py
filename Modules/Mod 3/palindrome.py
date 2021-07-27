s = "Was it a cat I saw?"
filtered = ""

# Solution uses extra space proportional to size of string "s
# s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
for letter in s:
    if not letter.isalnum() or letter.isspace():
        letter = ""
    filtered += letter.lower()       
# print(filtered == filtered[::-1])

letters = "aeiou"
print(letters - "a")
