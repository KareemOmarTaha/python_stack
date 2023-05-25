class User:
    def __init__(self , name , email):
        self.name = name
        self.email= email
        self.balance = 0
        return
    def make_deposit(self , amount):
        self.balance += amount 
        return self
    def make_withdraw (self , amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"User : {self.name} , Balance: {self.balance}")
        return self

Yazan = User("Yazan" , "sdfgdg43t34dg@gmail.com")
Yazan.make_deposit(1000).make_deposit(500).make_deposit(6000).make_withdraw(2000).display_user_balance()

Kareem = User("Kareem" , "324325435fdg@gmail.com")
Kareem.make_deposit(1000).make_deposit(10000).make_withdraw(5000).make_withdraw(5000).display_user_balance()

Muath = User ("Muath" , "dfghfdh545hg5g55bg@gmail.com")
Muath.make_deposit(10000).make_withdraw(5000).make_withdraw(1000).make_withdraw(2000).display_user_balance()

