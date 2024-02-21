
yazarlar = [
    "Orhan Pamuk",
    "Elif Safak",
    "Yasar Kemal",
    "Sabahattin Ali",
    "Ahmet Hamdi Tanpinar",
    "Nazim Hikmet",
    "Halide Edib Adıvar",
    "Cemal Sureyya",
    "Oguz Atay",
    "Can Yucel"
] 


yazarlar.sort(key = lambda x : x.split()[-1].lower(), reverse=True)

for i in yazarlar:
    print(i)