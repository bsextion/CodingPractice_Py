def firstIndex(arr, testVariable, currentIndex) :
    if len(arr) == currentIndex:
        return
    elif arr[currentIndex] == testVariable:
       return currentIndex
    else:
        return firstIndex(arr, testVariable, currentIndex+1)

print(firstIndex([9, 8, 1, 8, 1, 7], 1, 0))