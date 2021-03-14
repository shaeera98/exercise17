from bank_account import Account
from saving_account import Saving_Account
# from withdraw_error import Withdraw_Error
from attempt2 import Withdraw
from attempt2 import WithdrawError

joint_account = Account(9)
savings_account = Saving_Account(50)

print(joint_account.Withdraw(10))


print(joint_account.balance)