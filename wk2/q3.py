"""

Soru 3 :Müşteri Yönetim Sistemi
Proje Açıklaması: Bu proje, müşterilerinizi yönetmek ve temel işlemleri gerçekleştirmek için kullanabileceğiniz bir müşteri yönetim sistemi oluşturmanızı içerir. Bu sistem, müşteri bilgilerini saklama, yeni müşteri ekleyebilme, müşteri bilgilerini güncelleyebilme, müşteri silme ve müşteri listesini görüntüleme gibi temel işlevlere sahip olacaktır. İşte projenin temel adımları:

1-Müşteri bilgilerini saklamak için bir sözlük yapısı kullanın. Her müşteri için bir benzersiz müşteri kimliği (ID) atayın ve müşteri bilgilerini bu kimlikle ilişkilendirin. Her müşteri için ad, soyad, e-posta, telefon gibi bilgileri içeren bir sözlük kullanabilirsiniz.

2-Kullanıcıya aşağıdaki işlemleri seçebileceği bir menü sunun:

Yeni müşteri eklemek
Müşteri bilgilerini güncellemek
Müşteri silmek
Tüm müşterileri listelemek
Çıkış yapmak
3-Kullanıcının seçimine göre ilgili işlemi gerçekleştirin. Örneğin, yeni müşteri eklerken kullanıcıdan gerekli bilgileri alın ve sözlüğe yeni bir müşteri ekleyin.

4-Müşteri bilgilerini güncellerken, müşteri kimliğini kullanarak mevcut bilgileri görüntüleyin ve güncellenmiş bilgileri kaydedin.

5-Müşteri silme işleminde kullanıcıdan müşteri kimliğini alın ve bu müşteriyi sözlükten silin.

6-Tüm müşterileri listeleme işleminde, mevcut müşterilerin listesini görüntüleyin.

7-Kullanıcı çıkış yapana kadar işlemleri tekrarlayın.



Question 3: Customer Management System
Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers and viewing the customer list. Here are the basic steps of the project:

1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.

2-Provide a menu where the user can choose the following actions:

Add new customer
Update customer information
delete customer
List all customers
check out
3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.

4-When updating customer information, view the current information using the customer ID and save the updated information.

5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.

6-In the process of listing all customers, view the list of existing customers.

7-Repeat the process until the user logs out.

"""

# Using a dictionary structure to store customer information. Assigning a unique customer identification (ID) for 
# each customer and associate customer information with this ID. Using a dictionary containing information 
# such as name, surname, e-mail, phone number for each customer

customers = {}

def add_customer(customer_id, name, surname, email, phone_number):
    customers[customer_id] = {
        'name' : name,
        'surname' : surname,
        'email' : email,
        'phone_number' : phone_number
    }

    print("Customer added successfully!")

def get_customer_info(customer_id):
    return customers.get(customer_id, None)

def update_customer(customer_id, name=None, surname=None, email=None, phone_number=None):
    if customer_id in customers:
        if name:
            customers[customer_id]['name'] = name
        if surname:
            customers[customer_id]['surname'] = surname
        if email:
            customers[customer_id]['email'] = email
        if phone_number:
            customers[customer_id]['phone_number'] = phone_number
        print("Customer information updated successfully.")
    else:
        print("Customer ID not found.")

def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        print("Customer deleted successfully.")
    else:
        print("Customer ID not found")

def list_all_customers():
    if customers:
        print("List of all customers: ")
        for customer_id, customer_info in customers.items():
            print(f"Customer ID: {customer_id}, Name: {customer_info['name']}, Surname: {customer_info['surname']}, Email: {customer_info['email']}, Phone Number : {customer_info['phone_number']}")
    else:        
        print("No customers found.")

# 2-Providing a menu where the user can choose the following actions:
#Add new customer
#Update customer information
#delete customer
#List all customers
#check out


def menu():
    while True:
        print("\nCustomer Management System")
        print("1.Add new customer")
        print("2.Update customer information")
        print("3.Delete customer")
        print("4.List all customers")
        print("5.Check out")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            surname = input("Enter customer surname: ")
            email = input("Enter customer email: ")
            phone_number = input("Enter customer phone number: ")
            add_customer(customer_id, name, surname, email, phone_number)
        elif choice == '2':
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter updated name (press Enter to skip): ")
            surname = input("Enter updated surname (press Enter to skip): ")
            email = input("Enter updated email (press Enter to skip): ")
            phone_number = input("Enter updated phone number (press Enter to skip): ")
            update_customer(customer_id, name, surname, email, phone_number)
        elif choice == '3':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
        elif choice == '4':
            list_all_customers()
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()

