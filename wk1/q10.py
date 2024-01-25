#Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, 
#kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.
#(kilo indeks hesabı için internete bakabilirsiniz) Bunun için 
#kullanıcıdan kilo ve boy ölçülerini isteyiniz. 
#Kilo indeksi 25’in altında ise zayıf, 25-30 arasında ise normal, 
#30-40dan büyük ise kilolu, 
#40tan büyük ise aşırı kilolu sonuçlarına varsın.

height = float(input("Enter your height(Ex:1.72): "))
weight = float(input("Enter your weight(Ex:74.4): "))
BMI = weight/height**2


if BMI >= 30:
    print(f"Your body mass index is {BMI}, you have obesity.")
elif BMI >= 25:
    print(f"Your body mass index is {BMI}, you are overweight.")
elif BMI > 18.5:
    print(f"Your body mass index is {BMI}, you have normal weight.")
else:
    print(f"Your body mass index is {BMI}, you are underwight.")