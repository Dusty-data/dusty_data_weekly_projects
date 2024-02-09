n = int(input("Enter a number: "))
list = [19,34,62,93]
for i in list:
    if n > i:
        print(f"{n} is bigger than {i}. ")
    elif n < i:
        print(f"{n} is smaller than {i}. ")
    else:
        print(f"{n} is equal to {i}. ")