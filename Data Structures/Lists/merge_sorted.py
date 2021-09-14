def merge_lists(lst1, lst2):
    result = lst1+lst2
    pt1,pt2,ptr = 0,0,0

    while pt1 < len(lst1) and pt2 < len(lst2):
        if lst1[pt1] < lst2[pt2]:
            result[ptr] = lst1[pt1]
            pt1 += 1
        else:
            result[ptr] = lst2[pt2]
            pt2 += 1
        ptr += 1

    while pt1 < len(lst1):
        result[ptr] = lst1[pt1]
        pt1 += 1
        ptr += 1

    while pt2 < len(lst2):
        result[ptr] = lst2[pt2]
        pt2 += 1
        ptr += 1

    return result


merge_lists([3,4,5], [1,2,7])