def get_permutations(word):
    if word == "":
        return [""]
    permutations = []
    for letter in word:
        subpermuation = get_permutations(word.replace(letter,"",1))
        for perm in subpermuation:
            permutations.append(letter + perm)
    return permutations

get_permutations("ab")
