# nums = [10, 20, 30, 40, 50]
# nums_double = []

# for n in nums:
#     if n % 4 == 0:
#         nums_double.append(n * 2)

# nums_double = [n * 2 for n in nums if n % 4 == 0]
    
# nums_double = list(map(lambda n: n * 2, nums))

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)