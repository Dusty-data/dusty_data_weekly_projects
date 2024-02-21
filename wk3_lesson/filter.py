ulke_adlari = [
    "Türkiye",
    
    "",
    
    "Almanya",

    "Fransa",
    
    "",
    
    "İngiltere",
    
    "Japonya",
    
    "Çin",
    
    " ",
    
    "Rusya",
    
    "Brezilya"] 

#print(list(filter(lambda x : len(x)>1 , ulke_adlari )))

#print(list(filter(lambda x : x.strip() , ulke_adlari )))

a = list(filter(lambda x : len(x)>1 , ulke_adlari ))
ulke_adlari = list(filter(lambda x : x.strip() , a ))
print(ulke_adlari)