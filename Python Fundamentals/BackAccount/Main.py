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

Account_1 = BackAccount(0.05 , 0)
Account_1.deposit(1000).deposit(2000).deposit(3000).withdraw(500).yield_interst().display_account()

Account_2 = BackAccount(0.1 , 0)
Account_2.deposit(5000).deposit(2000).withdraw(3000).withdraw(2000).withdraw(4000).withdraw(7000).yield_interst().display_account()