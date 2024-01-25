# Bir kullanıcının girdiği üç sayının en büyüğünü bulan bir Python programı nasıl yazılır?

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

if n1 > n2 and n3:
    print(n1)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)