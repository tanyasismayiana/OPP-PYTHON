
class Account:
    def __init__(self,name,account_number):
        self.balance = 0
        self.name = name
        self.account_number= account_number
        self.



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
            
    def deposits_statements(self):
        for statements in self.deposits:
            print (statements)

                    
    def withdrawals_statements(self):
        for statement in self.deposits:
            print (statement)
        

    def current_balance(self):
        balance = self.balance
        return f"Your current is {balance}"        


