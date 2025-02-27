'''
Напишіть клас Банківський рахунок з атрибутами:
 ім'я клієнта
 баланс
 валюта
 словник з курсом валют(однаковий для всіх)
Додайте методи:
 вивід загальної інформації
 перевірка чи відома валюта(якщо ні, викликати
ValueError)
 перевести гроші з однієї валюти в іншу(ця операція
часто використовується, тому зрочно реалізувати
окремим методом)
 зміна валюти
 поповнення балансу(валюта та сама)
 зняття грошей з балансу(валюта та сама).
'''


class BankAccount:
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "UAH": 38.5,
        "GBP": 0.78
    }

    def __init__(self, client_name, balance, currency):
        self.client_name = client_name
        self.balance = balance
        self.currency = currency.upper()
        self._validate_currency(self.currency)

    def _validate_currency(self, currency):
        if currency not in self.exchange_rates:
            raise ValueError(f"Валюта {currency} не підтримується.")

    def get_info(self):
        return f"Клієнт: {self.client_name}, Баланс: {self.balance} {self.currency}"

    def convert_currency(self, amount, from_currency, to_currency):
        self._validate_currency(from_currency)
        self._validate_currency(to_currency)
        amount_in_usd = amount / self.exchange_rates[from_currency]
        return amount_in_usd * self.exchange_rates[to_currency]

    def change_currency(self, new_currency):
        new_currency = new_currency.upper()
        self._validate_currency(new_currency)
        self.balance = self.convert_currency(self.balance, self.currency, new_currency)
        self.currency = new_currency

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути більше 0.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути більше 0.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount


