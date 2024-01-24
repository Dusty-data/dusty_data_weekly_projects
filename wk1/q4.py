# Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu 
# ekrana yazdıran bir Python kodu yazınız.

number = int(input("Enter a number that you want to learn odd/even:" ))

if number % 2 == 0:
    print(f"The number that you entered is an even number.")
else:
    print(f"The number that you entered is an odd number.")
