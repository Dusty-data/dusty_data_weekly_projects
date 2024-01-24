# Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan 
#bir Python programı yazın. Faktöriyel, bir sayının kendisi ile 1 arasındaki 
# tüm pozitif tam sayıların çarpımıdır. Örneğin: kullanıcı 5 girdiyse program 
# şu çıktıyı vermeli: Kullanıcıdan bir sayı girin: 5 Faktöriyel: 120

number = int(input("Enter a positive number:"))

faktorial = 1

for i in range(1,number+1):
    faktorial *= i
    
print (f"faktorial of {number} is {faktorial}")
