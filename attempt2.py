# def withdraw(self, amount):
#     check_balance = self._balance - amount
#     if check_balance > 0:
#         self._balance -= amount
#         return f"Withdrawal successful - You have {self._balance} remaining"
#
#
# def withdraw_error(self, amount):
#     check_balance = self._balance - amount
#     if check_balance < 0:
#         raise self.withdraw_error(f'The maximum amount you can withdraw is {self._balance}')
#         # finally:
#         #     print("Unsuccessful")

from bank_account import Account


class WithdrawError(Exception):
    pass


class Withdraw(Account):
    def __init__(self, amount, initial_balance):
        super().__init__(amount, initial_balance)

    def withdraw(self, amount):
        check_balance = self._balance - amount
        if check_balance > 0:
            try:
                self._balance -= amount
                return f"Withdrawal successful - You have {self._balance} remaining"
            except WithdrawError:
                print('Withdrawal unsuccessful')
            finally:
                print(f'You can only withdraw {self._balance}')
