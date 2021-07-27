## get target and array of data
def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1
    
    while (low < high):
        mid = (low + high)//2
        if(target == data[mid]):
            return True
        elif(target < data[mid]):
            high = mid-1
        else:
            low = mid+1
    return False        

def binary_search_recursive(data, target, low, high):
    if low > target:
        return False
    else:
        mid = (low + high) //2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            binary_search_recursive(data, target, low, mid+1)
        else: 
            binary_search_recursive(data, target, mid+1, high)

def closet_num(data, target, low, high, closet):
    if low > target:
        return closet
    else:
        mid = (low + high) //2
        if data[mid] == target:
            return data[mid]
        
        left_mid = target - data[mid-1]
        right_mid = target - data[mid+1]
        
        if left_mid < right_mid:
            closet_num(data, target, low, mid-1, data[mid-1])
        else: 
            closet_num(data, target, mid+1, high, data[mid+1])                 

        
        
    
    
sample = [1,4,5,6,8,9,11,13,15]
# binary_search_iterative(sample, 5 )
closet_num(sample, 5, 0, (len(sample))-1, None )