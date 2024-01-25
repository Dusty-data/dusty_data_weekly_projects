# Soru 12 : Bir ogrenciden herhangi bir ders icin Vize ve Final notlarıni alin. 
# Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını 
#verecektir. Ortalama 50'nin altında ise ekranda “BAŞARISIZ”, 
#50 ve üzerinde ise “BAŞARILI” çıktısı ekrana gelecektir. 
#Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.

for i in range(4):

    visa_grade = float(input(f"Enter {i + 1}. lesson visa grade(Ex.:71.5): "))
    final_grade = float(input(f"Enter {i + 1}. lesson final grade(Ex.:66.4): "))
    avg_end_grade = (visa_grade*0.4) + (final_grade*0.6)

    if final_grade <= 50:
        print(f"{i + 1}. ders BAŞARISIZ")
    else:
        print(f"{i + 1}. ders BAŞARILI")