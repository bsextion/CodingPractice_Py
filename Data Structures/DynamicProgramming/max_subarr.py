def find_max_sum_sub_array(A):
    max_sum = A[0]
    result_arr = [max_sum]

    for i in range(1, len(A)):
        if max_sum + A[i] > A[i]:
            max_sum += A[i]
        else:
            max_sum = A[i]

        result_arr.append(max_sum)

    result_arr = sorted(result_arr)
    return result_arr[-1]

print(find_max_sum_sub_array([-4,2,-5,1,2,3,6,-5,1]))