def rearrange(lst):
    even_list = list(filter(lambda x: x % 2 == 0, lst))
    odd_list = list(filter(lambda x: x % 2 != 0, lst))
    odd_list.extend(even_list)

    return odd_list

print(rearrange([-1, 2, -3, -4, 5]))