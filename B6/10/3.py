class Wallet:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return f'Клиент: {self.name}. Баланс {self.balance}.'


john = Wallet('John', 50)
print(john.get_balance())