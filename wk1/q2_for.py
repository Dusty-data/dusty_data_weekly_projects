# Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan çift sayıları ekrana yazdıran 
# bir Python programı yazın. Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.

number = int(input(f"Enter a number: "))

print(f"For loop even numbers till your choose:")
for i in range(number+1):
    if i % 2 == 0:
        print(i)