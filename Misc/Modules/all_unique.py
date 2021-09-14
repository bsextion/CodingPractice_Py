def is_unique(input_str):
  input_str = input_str.lower()
  
  map = dict()
  for letter in input_str:
      if letter in map:
          return False
      else:
          map[letter] = 1
  
  return True             
      
      
      