#Sort the array in place
#Create a for loop
#Beginning at index 0, check if number == n+1,
#If number is correct, do nothing
#If number is not correct, swap with n+1
#hold num in temp variable, n[i] = n[temp], n[temp] = temp
#Do this until end of loop

def cyclic_sort(nums):
  for i in range(0, len(nums)):
      num = nums[i]
      while num != i+1:
          temp = num
          nums[i] = nums[temp-1]
          nums[temp-1] = temp
          num = nums[i]
                  
  return nums


cyclic_sort([1, 5, 6, 4, 3, 2])