#**Problem**#
#Find the average of all contiguous subarrays of size K in the given array.


#Solution 1
#1) For size k, get the first k elements in array
#2) Calculate the average for k elements and store in new array
#3) Slide the array and repeat 1-2
#4 Continue until we cannot create more subarray of size k
def find_averages_of_subarrays_s1(K, arr):
    start = 0
    avg_arr = []
    
    while(K <= len(arr)):
        k_arr = arr[start:K]
        avg_arr.append(sum(k_arr)/len(k_arr))
        start += 1
        K += 1
        
#Solution 2
#1) For size k, get the first k elements in array
#2) Calculate the sum and store in variable,
#3) Calculate the average and store in array
#3) subtract the S from the sum and add K+1
#4) Repeat 1-3
#4) Continue until we cannot create more subarray of size k
def find_averages_of_subarrays_s2(K, arr):
    start, sumArr = 0, 0
    avg_arr = []
    k_arr = arr[start:K]
    sumNum = sum(k_arr)
    
    while(K < len(arr)):
        avg_arr.append(sumNum/len(k_arr))
        sumNum -=arr[start]
        sumNum += arr[K]
        start += 1
        K += 1
    avg_arr.append(sumNum/len(k_arr))
    
    return avg_arr        



        
        
    
find_averages_of_subarrays_s2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
