#Question 1
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 

s = Bank_Account()
   

for i in range(1,5):
    s.deposit()
    s.withdraw()
    s.display()

#Question 2

import math
class cone():
    def __init__(self,radius):
        self.radius=radius
        self.height=2
       
    def volume(self):
        return math.pi*(self.radius**2)
   
    def surface(self):
        base= math.pi*(self.radius**2)
        side= math.pi*((self.radius**2+self.height**2))**0.5
        return(base+side)
 
r=int(input("Enter radius of circle: "))
obj=cone(r)
print("volume:",round(obj.volume(),2))

print("surface area:",round(obj.surface(),2))
