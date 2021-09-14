# for i in range(1, 11):  # A sequence from 1 to 10
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")
# for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
#     print(i)        

nums_list = [2,4,5,6,8,9]
# for i in range(0, len(nums_list)):
#     nums_list[i] = nums_list[i]*2
# print(nums_list) 

# for num in nums_list:
#     print(num)

for n1 in nums_list:
    for n2 in nums_list:  # Now we have two iterators
        if(n1 + n2 == n):
            print(n1, n2)   