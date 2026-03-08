#Class + First objects(01.03.26) - create a class called BankAccount that has two attributes: owner and balance.
class BankAccount:
    pass

account1 = BankAccount()
account2 = BankAccount()

account1.owner = "Mimmi"
account1.balance = 1000
account2.owner = "Alex"
account2.balance = 500

print(account1.owner, account1.balance)
print(account2.owner, account2.balance)



#Automatic Object Setup(02.03.26) - create a class called BankAccount that has two attributes: owner and balance. 
# Then create two objects from the class and print the values of their attributes.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account1 = BankAccount("Mimmi", 1000)
account2 = BankAccount("Alex", 500)

print(account1.owner, account1.balance)
print(account2.owner, account2.balance)



#Updated version (03.03.26)
class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.balance = balance
        def show_balance(self):
             print('Balance:', self.balance)
        def deposit(self, amount):               #added deposit method to show behaviour between objects
               self.balance = self.balance + amount


account1 = BankAccount('Mila', 200)
account1.deposit(500)
account2 = BankAccount('Alfred', 400)
account2.deposit(900)

account1.show_balance()
account2.show_balance()


#This program defines a BankAccount class with methods to deposit, withdraw, and show balance
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited", amount)

    def withdraw(self, amount):
        if amount > self.balance:    #check if the amount to withdraw is greater than the current balance
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount 
            print("Withdrew", amount)

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(100)

account.show_balance()
account.deposit(30)
account.withdraw(10)
account.withdraw(500)
account.show_balance()