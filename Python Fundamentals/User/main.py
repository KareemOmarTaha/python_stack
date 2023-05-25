class User:
    def __init__(self , name , email):
        self.name = name
        self.email= email
        self.balance = 0
    def make_deposit(self , amount):
        self.balance += amount 
    def make_withdraw (self , amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"User : {self.name} , Balance: {self.balance}")

Yazan = User("Yazan" , "sdfgdg43t34dg@gmail.com")
Yazan.make_deposit(500)
Yazan.make_deposit(1000)
Yazan.make_deposit(6000)
Yazan.make_withdraw(2000)
Yazan.display_user_balance()

Kareem = User("Kareem" , "324325435fdg@gmail.com")
Kareem.make_deposit(1000)
Kareem.make_deposit(10000)
Kareem.make_withdraw(5000)
Kareem.make_withdraw(5000)
Kareem.display_user_balance()


Muath = User ("Muath" , "dfghfdh545hg5g55bg@gmail.com")
Muath.make_deposit(10000)
Muath.make_withdraw(5000)
Muath.make_withdraw(1000)
Muath.make_withdraw(2000)
Muath.display_user_balance()

