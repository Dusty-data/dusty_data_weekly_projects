def combine(**kwargs):
    result = ""

    for i,j in kwargs.items():
        result +=i +"\t " + j +"\n"

    return result

sozluk={}

print(combine(**sozluk))