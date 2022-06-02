class Bank:
    def __init__(self,account_name,account_number,pin,balance,account_type):
        self.account_name=account_name
        self.account_number=account_number
        self.pin=pin
        self.balance=balance
        self.account_type=account_type

    def deposit(self,amount):
        new_bal= amount+self.balance
        return new_bal

    def withdraw(self,amount):
        new_balance=amount-self.balance
        return new_balance        
