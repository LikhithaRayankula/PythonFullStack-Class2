class Account:
    def __init__(self, name, age):
            self.name = name
            self.age = age
            self.__balance = 0
    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        self.__balance += balance

acc=Account("John", 10)
print(acc.get_balance())
acc.set_balance(100)
print(acc.get_balance())
print(acc.__balance()) #because balance is a private variable