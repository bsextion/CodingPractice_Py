class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in map:
                map[sorted_word].append(word)
            else:
                map[sorted_word] = [word]

        for value in map.values():
            result.append(value)

        return result

Solution.groupAnagrams("", [""])