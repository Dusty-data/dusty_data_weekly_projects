# 1-10 arası sayıyı tahmine eden oyun

n = 4
predict = 0

while True:
    predict += 1
    x = int(input("Enter a number to find my number: "))

    if x > n:
        print("Enter a smaller one")
        

    elif x < n:
        print("Enter a bigger one")
        
    
    else:
        
        print(f"You have found the number in my mind with a number of {predict} ")
        break