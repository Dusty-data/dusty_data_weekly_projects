def number(*args):
    numbers = []
    for i in args:
        i+= 5
        numbers.append(i)
    return numbers

print(number(1,2,4,7))