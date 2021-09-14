def merge_lists(lst1, lst2):
    result = []
    ptr1, ptr2, rstptr = 0, 0, 0

    while (ptr1 < len(lst1) and ptr2 < len(lst2)):
        if lst1[ptr1] < lst2[ptr2]:
            result.append(lst1[ptr1])
            ptr1 += 1
            rstptr += 1
        else:
            result.append(lst2[ptr2])
            ptr2 += 1
            rstptr += 1

    while ptr1 < len(lst1):
        result.append(lst1[ptr1])
        ptr1 += 1
        rstptr += 1

    while ptr2 < len(lst2):
        result.append(lst2[ptr2])
        ptr2 += 1
        rstptr += 1

    return result

merge_lists([1,3,4,5], [2,6,7,8])