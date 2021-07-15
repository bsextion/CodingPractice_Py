# times = lambda num : num * 3
# show = lambda a,b,c: a[0] + b[0] + c[0]
# compare = lambda num: True if num >= 20 else False

# print(compare(15))
# print(show("Hello", "It's", "Me"))
# print(times(4))


numbers = [0,1,2,3,4]
five_numbers = map(lambda n: n * 5, numbers)
even_numbers = filter(lambda n: n % 2 == 0, numbers)

print(list(five_numbers))
print(list(even_numbers))