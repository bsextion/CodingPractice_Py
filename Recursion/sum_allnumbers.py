def sumTill(targetNumber) :
    if targetNumber == 1:
        return targetNumber
    return targetNumber + sumTill(targetNumber-1)

print(sumTill(5))
