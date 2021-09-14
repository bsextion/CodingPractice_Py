#remove even
def remove_even(lst):
    lst = list(filter(lambda x: x%2 != 0, lst))
    return lst

def remove_even(lst):
    lst = [x for x in lst if x % 2 != 0]
    return lst
