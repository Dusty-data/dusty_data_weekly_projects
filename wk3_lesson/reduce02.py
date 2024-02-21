from functools import reduce

#reduce(function, iterable, initial)

numbers = [1,6,3,7,34,3,8,5]
#word= ["H", "a", "l", "i", "l"]

print(reduce(lambda x , y : x if x>y else  y if y>x else y, numbers))