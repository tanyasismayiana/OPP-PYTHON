# class Bank:
#     def __init__(self,account_name,account_number,pin,balance,account_type):
#         self.account_name=account_name
#         self.account_number=account_number
#         self.pin=pin
#         self.balance=balance
#         self.account_type=account_type

#     def deposit(self,amount):
#         new_bal= amount+self.balance
#         return new_bal

#     def withdraw(self,amount):
#         new_balance=amount-self.balance
#         return new_balance   
# 
# import re
# from unicodedata import name


# class Account:
#     def__init__(self,name,account_number):
#     self.balance=0
#     self.name=name
#     self.account_number=account_number

#     def deposit(self,amount):
#         self.balance +=amount 
#         return f"you have deposited {self.amoont} and your new balance is {self.balance}"


import re
from unicodedata import name
# from unicodedata import name

class Account:
    def __init__(self,name,account_number):
        self.balance = 0
        self.name = name
        self.account_number= account_number



    def deposit(self,amount):
        
        if amount <0 :
          return f"Deposit amount should be more than zero"
        else:
            self.balance +=amount 
            return f"You have deposited {amount} your balance is {self.balance}"
            

    def withdraw(self, amount):
        if amount >self.balance:
            return f"your balance is {self.balance} you cannot withdraw {amount}"
        elif amount<=0:
            return f"your account must be more than zero to be able to withdraw"
        else:
            self.balance-=amount
            return f"You have withdrawn {amount} your new balance is {self.balance}"

