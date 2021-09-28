def find_string_anagrams(str, pattern):
    result_indexes = []
    # sorted_pattern =  ''.join(pattern.sort())
    sorted_pattern = ''.join(sorted(pattern))
    start = 0
    end = len(pattern)

    while end <= len(str):
        word = ''.join(sorted(str[start:end]))
        if word == sorted_pattern:
            result_indexes.append(start)
        start += 1
        end += 1
    return result_indexes

find_string_anagrams("abbcabc", "abc")
