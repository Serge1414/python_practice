class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата карткою {amount}{self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount}{self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount}{self.currency}")


def create_payment():
    payment_type = input("Введіть тип платежу (credit, paypal, crypto): ").strip().lower()
    currency = input("Введіть валюту: ")

    if payment_type == "credit":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Невідомий тип платежу!")
        return None


payments = []
for _ in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)

