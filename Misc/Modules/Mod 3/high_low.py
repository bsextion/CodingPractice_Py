def count_low_high(num_list):
    if len(num_list) == 0:
        return None
    
    high = set(list(filter(lambda n: n> 50 or n % 3 == 0, num_list)))
    low = set(num_list).difference(high)
    
    return [len(low), len(high)]

   
           
            
count_low_high([20, 9, 51, 81, 50, 42, 77])            