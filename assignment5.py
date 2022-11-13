#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Challenge 1
# Square of Sum
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def SqSum(self):
        self.sqx=self.x**2
        self.sqy=self.y**2
        self.sqz=self.z**2
        return self.sqx+self.sqy+self.sqz
b=Point(1,3,5)
print(b.SqSum())


# In[6]:


#challenge 2
# Calculator
class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def substract(self):
        return self.num2-self.num1
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num2/self.num1
c=Calculator(10,94)
print(c.add())
print(c.substract())
print(c.multiply())
print(c.divide())


# In[8]:


#challenge 3
# Complete Student Class
class Student:
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollno):
        self.__rollno=rollno
    def getRollNumber(self):
        return self.__rollno
s=Student()
s.setName("jappan")
print(s.getName())
s.setRollNumber(10)
print(s.getRollNumber())


# In[12]:


# Challenge 4
# Parent and child class
class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,InterestRate=0):
        super().__init__(title, balance)
        self.title=title
        self.balance=balance
        self.InterestRate=InterestRate

print("Account Details")
A=Account("Asish", 5000)
print(f"Name of the Account Holder is {A.title}")
print(f"Available Balance is {A.balance} Rs")
print(f"Here, {A.title} is the title, {A.balance} is the balance . ")
print("***************************************************************************************")
print("Savings Account Details")
SA=SavingsAccount("Asish", 5000, 5)
print(f"Name of the Account Holder is {SA.title}")
print(f"Available Balance is {SA.balance} Rs")
print(f"Name of the Account Holder is {A.title}")
print(f"Interest Rate on Current Balance in percent is {SA.InterestRate}")
print(f"Here, {SA.title} is the title, {SA.balance} is the balance and {SA.InterestRate} is the interestRate .")


# In[17]:


#Challenge 5
# handling bank account
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance=self.balance - amount
        
    
    def deposit(self, amount):
       self.balance=self.balance + amount 
       
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance*self.interestRate)/100
s=SavingsAccount("Asish",2000)
s.deposit(500)
s.getBalance()
print(s.getBalance())

p=SavingsAccount("Asish",2000)
p.withdrawal(500)
p.getBalance()
print(p.getBalance())

Si=SavingsAccount("Asish",2000,5)
print(Si.interestAmount())


# In[ ]:




