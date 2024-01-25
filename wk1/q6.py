# Kullanıcıdan bir sayı alan ve bu sayının 
# asal olup olmadığını kontrol eden bir Python kodu yazınız.
 
number = int(input("Enter a number that you want to check that is a prime number: "))

if number < 2:
    print(f"The number {number} that you enter is not a prime number.")

else:
    for i in range(2, number):
        if number % i == 0:
            print(f"The number {number} that you enter is not a prime number.")
            break

        else:
            print(f"The number {number} that you enter is a prime number.")
            break
