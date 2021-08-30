
def canConstruct(word, wordbank):
    if word == "":
        return True

    for w in wordbank:
        if word.startswith(w):
            suffix = word[len(w):]
            if canConstruct(suffix, wordbank) == True:
                return True

    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

