# cm ve dm değerlerinin toplamını metreye çeviren program
# 1 dm = 0.1 m # 1 cm = 0.01 m

def meter(dm  = 0 , cm = 0):
    dm_to_m = 0.1 * dm
    cm_to_m = 0.01 * cm
    return dm_to_m + cm_to_m
    
print(meter(100))