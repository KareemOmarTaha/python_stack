class BackAccount:
    def __init__(self , int_rate, balance):
        self.int_rate = int_rate 
        self.balance = balance 
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    def display_account(self):
        print (f"Balance : {self.balance}")
        return self
    def yield_interst(self):
        if self.balance > 0:
            self.balance = self.balance+(self.balance*self.int_rate)
        return self 


class User:
    def __init__(self , name , email, int_rate , balance):
        self.name = name
        self.email= email
        self.account = BackAccount(int_rate , balance)

Yazan = User("Yazan" , "sdfgdg43t34dg@gmail.com", 0.1 , 0)
Yazan.account.deposit(1000).deposit(500).deposit(6000).withdraw(2000).yield_interst().display_account()

