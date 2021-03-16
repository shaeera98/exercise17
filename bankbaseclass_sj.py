from InsufficientFundsException import InsufficientFundsException
    
class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = float(balance)
            
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsException (f"You do not have sufficient funds to make this withdrawal. The maximum you can withdraw is {self._balance}")
        else:
            self._balance -= amount
            return self._balance

    def getbalance(self):
        return self._balance


    # @property
    # def id(self):
    #     return self._name, self._account_number

    # @id.getter
    # def id(self, name, account_number):
    #     self._name = name.Title()

    # @balance.getter
    # def balance(self, balance):
    #     self._balance = balance

#     # def __str__(self): ???
#     #     return 'account {} current balance is £{}'.format(self.name, self._balance)

        



