def findSquare(targetNumber):
    if targetNumber == 0:
        return 0
    if targetNumber <= 1:
        return 5

    return 5 + findSquare(targetNumber-1)

print(findSquare(5))

