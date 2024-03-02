
class Book:
    language = "Turkce"
    
    def __init__(self, title, author, number_of_page):
        self.title = title
        self.author = author
        self.number_of_page = number_of_page
  
    def display_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Number of page: {self.number_of_page}")

    def increase_number(self, increase):
        self.number_of_page += increase

    def decrease_number(self, decrease):
        self.number_of_page -= decrease

    def change_language(self, new_language):
        self.language = new_language


book1 = Book("Beyaz Zambaklar Ülkesinde", "Grigory Petrov", 256)
book2 = Book("Kürk Mantolu Madonna", "Sabahattin Ali", 184)
book3 = Book("Saatleri Ayarlama Enstitüsü", "Ahmet Hamdi Tanpınar", 328)


book2.increase_number(20)
book2.decrease_number(10)
book2.display_info()

#print(book1.language)
#print(book2.display_info())

book2.change_language("Dutch")
print(book2.language)











        


