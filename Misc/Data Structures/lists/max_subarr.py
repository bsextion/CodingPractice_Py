
# start by setting max_sum to the first element in list
# result list initially only holds the first element

# for each element in the arr:
# check if max_sum + arr[i] is less than arr[i], if so max_sum = arr[i], else max[sum] + arr[i]
# add the max_sum to the result array

#sort the array, and grab the last index

def find_max_sum_sublist(lst):
    max_sum = lst[0]
    result = [max_sum]

    for i in range(1, len(lst)):
        if max_sum + lst[i] < lst[i]:
            max_sum = lst[i]

        else:
            max_sum += lst[i]

        result.append(max_sum)

    result.sort()
    return result[-1]

find_max_sum_sublist([-2,10,7,-5,15,6])