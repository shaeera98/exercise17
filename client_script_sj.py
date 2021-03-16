from bankbaseclass import Account
from InsufficientFundsException import InsufficientFundsException
from NotWithdrawalException import NotWithdrawalException
from annual_saver import Annual_saver
import datetime


john = Account("John", 1000)
print(f'{john._name} your current balance is {john._balance}')

try:
    john.withdraw(890)
except InsufficientFundsException as err:
    print(err)
else: 
    print(f"Your new balance is £", john._balance)

gavin = Annual_saver("Gavin", 2000, "2020-10-16")

try:
    gavin.annual_withdrawal(datetime.date.today, 300)
    # gavin.withdraw(9800)
except NotWithdrawalException as err:
    print(err)
else:
    print(gavin.balance)




