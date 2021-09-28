#Generate an array so that find_min function returns the wrong answer
#Find the minimum positive number not in the array
#Split the string into substring so that each letter only appears once


def find_min(A:[]):
    ans = 0
    for i in range(1, len(A)):
        if A[i] < ans:
            ans = A[i]
    return ans


def solution(N):
    result = [1] * N
    result[0] = -1
    return result
    #write a function, where we create an array with n numbers set to 1,
    #first postiobn will always be set to -1

arr = solution(1)
find_min(arr)

