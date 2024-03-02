class Customer:
    def __init__(self, name, surname, nl_identification, phone):
        self.name = name
        self.surname = surname
        self.nl_identification = nl_identification
        self.phone = phone

    def display_information(self):
        print("Customer Information:")
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("NL ID Number:", self.nl_identification)
        print("Phone Number:", self.phone)


class Account(Customer):
    def __init__(self, name, surname, nl_identification, phone, account_number, initial_balance=0):
        super().__init__(name, surname, nl_identification, phone)
        self.account_number = account_number
        self.balance = initial_balance

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited {amount} Euro. New balance: {self.balance} Euro")

    def money_check(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} Euro. New balance: {self.balance} Euro")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Balance: {self.balance} Euro")


# Create a Customer object
customer = Customer("John", "Doe", "1234567890", "555-123-4567")
customer.display_information()

# Create an Account object and add customer information
account = Account("John", "Doe", "1234567890", "555-123-4567", "123456789", initial_balance=1000)

# Perform account operations
account.deposit_money(500)
account.money_check(200)
account.money_check(2000)  # This should display "Insufficient funds."
account.display_balance()