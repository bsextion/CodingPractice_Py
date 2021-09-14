def recursive_multiply(x, y):
  if y == 1:
    return x
  x += x
  return recursive_multiply(x, y-1)
  
  
print(recursive_multiply(5,2))
    
    
    