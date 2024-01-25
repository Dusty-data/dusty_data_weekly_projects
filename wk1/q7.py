# Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar olan sayıları 
# içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?

#i = 0

#for i in range(1,20):
#    i += (i+1)
#   print(i)

"""
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
"""

limit = int(input("How many fibonacci number do you want to see? "))
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(limit-2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3


