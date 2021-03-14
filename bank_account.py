from withdraw_error import Withdraw_Error


class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    # def withdraw(self, amount):
    #     if amount > 0:
    #         check_balance = self._balance - amount
    #         # if check_balance < 0:
    #         #     return f"Withdrawal unsuccessful - the maximum amount you can withdraw is {self._balance}"
    #         # else:
    #         if check_balance > 0:
    #             self._balance = amount
    #             return f"Withdrawal successful"
    #     self._balance -= amount
    #     return self._balance

    # def withdraw(self, amount):
    #     check_balance = self._balance - amount
    #     if check_balance > 0:
    #         self._balance -= amount
    #         return f"Withdrawal successful - You have {self._balance} remaining"
    #
    # def withdraw_error(self, amount):
    #     check_balance = self._balance - amount
    #     if check_balance < 0:
    #         raise self.withdraw_error(f'The maximum amount you can withdraw is {self._balance}')
    #         # finally:
    #         #     print("Unsuccessful")

    @property
    def balance(self):
        return self._balance