from bank_account import Account


# class Saving_Account(Account):
#     def __init__(self, initial_balance):
#         super().__init__(initial_balance)

# def withdrawn(self, amount):
#     if amount > 0:
#         check_balance = self._balance - amount
#         if check_balance < 0:
#             return f"Withdrawal unsuccessful - the maximum amount you can withdraw is {self._balance}"
#         else:
#             self._balance = amount
#             return f"Withdrawal successful"
#     self._balance -= amount
#     return self._balance

# class Withdraw_Error(Exception):
#     def __init__(self, amount):
#             check_balance = self._balance - amount
#             if check_balance < 0:
#                 raise self.withdraw_error(f'The maximum amount you can withdraw is {self._balance}')
#
# class