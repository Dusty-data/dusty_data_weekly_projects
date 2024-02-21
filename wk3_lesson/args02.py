def addition(*args):
    result = 0
    for i in args:
        result += i
    return result

numbers = (1,2,3,4,5,6,7)

print(addition(*numbers))