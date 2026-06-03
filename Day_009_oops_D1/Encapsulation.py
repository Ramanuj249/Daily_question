class Person:
    def __init__(self):
        self.name = "john"          # Public: accessible anywhere
        self._name = "John"         # Protected: accessible inside class & subclass
        self.__name = "John"        # Private: accessible ONLY inside class


class BankAccount:
    def __init__(self, balance, owner):
        self.__balance=balance              # Private
        self.owner = owner                  # Public
        self._bank_name = "ABC BANK"        # Protected

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance -= amount
        else:
            print("not enough balance")

    def get_balance(self):
        return self.__balance
    # encapsulation means — data is protected, only accessible through methods! 💪

    def show_details(self):
        # accessing all three inside class — all work ✅
        print(f"Owner: {self.owner}")
        print(f"Bank: {self._bank_name}")
        print(f"Balance: {self.__balance}")

shivam = BankAccount(10000, "ramanuj")
# shivam.deposit(10000)
# print(shivam.get_balance())
# shivam.withdraw(10000)
# print(shivam.get_balance())

shivam.show_details()
