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



