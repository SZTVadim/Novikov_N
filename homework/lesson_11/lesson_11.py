# Задание 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book1 = Book("Девушка с татуировкой дракона", "Стиг Ларссон", 576)
book2 = Book("Стигматы Палмера Элдрича", "Филип Дик", 352)
book3 = Book("Колыбель для кошки", "Курт Вонегут", 288)
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
print(book1.is_long())
print(book2.is_long())
print(book3.is_long())


# Задание 2
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Виталик")
account.deposit(1000)
account.withdraw(100)
account.withdraw(1200)
print(account.get_balance())
