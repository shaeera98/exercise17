from bank_account import Account


class Saving_Account(Account):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)

    def deposit(self, amount):
        self._balance += amount
        if amount < 500:
            return f"You would like to deposit {amount}. Your overall balance is {self._balance}."
        else:
            print("Deposit unsuccessful - For amounts over £500 Please speak to the bank")
            self._balance = amount