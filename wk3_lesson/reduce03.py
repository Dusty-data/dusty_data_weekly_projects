from functools import reduce

number = range(1,6)

print(reduce(lambda x, y : x*y, number))