# Kullanıcıdan bir başlangıç ve bitiş değeri alan ve bu değerler arasındaki 
# tüm sayıları ekrana yazdıran bir Python kodu yazınız(bitis degeri dahil).

begin_number = int(input("Enter a begin number:"))
end_number = int(input("Enter an end number:"))

for i in range(begin_number+1,end_number):
    print(i)
