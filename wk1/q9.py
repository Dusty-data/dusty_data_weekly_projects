#  Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom 
# (tersten okunduğunda aynı olan) olup olmadığını kontrol eden bir döngü 
# ve koşullu ifade kombinasyonu nasıl oluşturulur?

word = input("Enter a word that you want to check that is same with the reversed or not: ")

reversed_word = word[::-1]

if reversed_word == word:
    print(f"The reversed of {word} is the same.")
else:
    print(f"Find another word. The {reversed_word} is different than {word}.")