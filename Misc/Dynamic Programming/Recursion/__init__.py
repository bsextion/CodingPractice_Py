def permute(word, result, current, remaining):
    if len(word) == len(current) and remaining == "":
        result.append(current)
        return
    if len(word) == len(current):
        return

    for letter in word:
        temp = current + letter
        permute(word, result, temp, word.replace(letter, "",1))




class Solution(object):
    def permutations(self, word):
        result = []
        permute(word, result, "", word)
        return result






Solution.permutations("","abc")