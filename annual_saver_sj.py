from InsufficientFundsException import InsufficientFundsException
from NotWithdrawalException import NotWithdrawalException
from bankbaseclass import Account
import datetime

class Annual_saver(Account):
    def __init__(self, name, balance, opening_date):
        super().__init__(name, balance)
        self.name = name
        self.balance = balance
        self.opening_date = opening_date
      
    
    def annual_withdrawal(self, date, amount):
        if date != self.opening_date:
            raise NotWithdrawalException (f'Withdrawal not possible, withdrawal date only on yearly anniversary of opening ie {self.opening_date}')
        else:
            # withdrawal test here
            self.balance -= amount
            return self.balance


