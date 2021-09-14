def find_max_sum_sublist(lst):
    max_sum = lst[0]
    curr_sum = lst[0]

    for i,num in enumerate(lst, start=1):
        if i == len(lst):
            break
        if curr_sum + lst[i] < lst[i]:
            curr_sum = lst[i]
        else:
            curr_sum += lst[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(find_max_sum_sublist([-4,2,-5,1,2,3,6,-5,1]))