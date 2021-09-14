import random
import string


class Codec:
    def __init__(self):
        self.nums_char = list(string.ascii_letters) + list(range(0, 10))
        self.encodeMap = dict() # empty map of long url to short
        self.decodeMap = dict()

    def encode(self, longUrl: str) -> str:
        if not longUrl in self.encodeMap:
            tiny = ''.join(str(random.choice(self.nums_char)) for x in range(0,6))
        shorturl = "http: // tinyurl.com/"+tiny
        self.encodeMap[longUrl] = shorturl
        self.decodeMap[shorturl] = longUrl
        return shorturl


    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.decodeMap:
            return self.decodeMap[shortUrl]
        else:
            return ""


url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))