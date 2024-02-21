
from functools import reduce

#reduce(function, iterable, initial)

numbers = [1,2,3,4,5,6,7,8,9,10]
word= ["H", "a", "l", "i", "l"]

print(reduce(lambda x , y : x+y, word))

