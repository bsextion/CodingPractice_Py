import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                      "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...",
                      "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letters = list(string.ascii_lowercase)
        map = dict(zip(letters, morse_code))
        result = set()

        for word in words:
            temp = ''.join(map[w] for w in word)
            result.add(temp)
        return len(result)


