from datetime import datetime
class Account:
    def __init__(self,name,acc_number):
      self.balance=0
      self.name=name
      self.acc_number=acc_number
      self.deposits=[]
      self.withdrawals=[]
      self.date=datetime.now()
      self.loan_balance=0
    def deposit(self,amount):
        if amount <=0:
         return f"Deposited amount, should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append({"date":datetime.now("%C"),"amount":amount,"narration":"Deposit"})
        return f"Hello{self.name}, you have deposited{amount} your balance is {self.balance}"
    def withdraw(self,amount):
        if amount>self.balance:
           return f"Your balance is {self.balance} , you cannot withdraw the {amount}"
        elif amount <=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            self.withdrawals.append({"date":datetime.now("%C"),"amount":amount,"narration":"Withdral"})

            return f"You have withdrawn {amount} your balance is {self.balance}"
    def deposit_statement(self):
        print(*self.deposits,sep="\n")
    def withdraw_statement(self):
        print(*self.withdrawals,sep="\n")

    def full_statement(self):
        full_statements=self.deposits + self.withdrawals 
        for statement in full_statements:
            print(full_statements)


    def borrow(self,amount):
        sum=0
        for statement in self.deposits:
            sum+=statement["amount"]
    
        if (len (self.deposit))<10:
            print("You are unable to withdraw due to less deposits")
        
        elif amount<100:
            print("You are unable to borrow due to the amount stated.")

        elif amount > (sum//3):
            print("fcfttc6i7frdf46es")
        elif self.balance<=0:
            print("You are uneble to borrow since your account balance is 0 ")
        
        elif  self.loan_balance >0:
            print("You can not access the loan since you have an outstanding loan")
        
        else:
            self.loan_balance+=(amount(amount*0.03))
            print(f"Your oustanding balance is {self.loan_balance}")      


    def loan_repayment(self,amount):
        over_payment=amount-self.loan_balance
        loan_payment=amount-over_payment
        if amount<0:
            print("your repayment loan has to be more than 0")
        
        elif amount<self.loan_balance:
            self.balance-=amount
            print(f"The {amount} was deducted to repay your loan")
       
        else:
             self.balance+=over_payment
             self.loan_balance-=loan_payment
        print(f"You have successfully finish to pay you loan the balance is in your account is {self.balance}")
    

    def transfer(self, amount,account_two):
        if amount>self.balance:
            print("You are unable to transfer since your have insefficient balance")
        elif amount<=0:
            print("You need to have more than 0 amount to be able to transfer")
        else:    
            account_two.balance+=amount 
            self.balance-=amount
            print(f"You have received {account_two.balance} from {self.name} ")    





            




