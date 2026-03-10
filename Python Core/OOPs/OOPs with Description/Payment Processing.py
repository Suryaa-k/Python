# You are developing a payment processing module for an e-commerce website.
# The system supports multiple payment methods, and each payment method follows a
# different processing flow.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    def _validate_payment(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero")
        print("Payment validation successful")
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        self._validate_payment(amount)  # reuse shared validation
        print(f"Processing credit card payment of ₹{amount}")
        print("Credit card charged successfully\n")

class UPIPayment(PaymentProcessor):
    def process_payment(self, amount):
        self._validate_payment(amount)
        print(f"Processing UPI payment of ₹{amount}")
        print("UPI transaction successful\n")

class WalletPayment(PaymentProcessor):
    def process_payment(self, amount):
        self._validate_payment(amount)
        print(f"Processing wallet payment of ₹{amount}")
        print("Wallet payment completed\n")

def process_all_payments(payments, amount):
    for payment in payments:
        payment.process_payment(amount)


credit = CreditCardPayment()
upi = UPIPayment()
wallet = WalletPayment()

payments = (credit, upi, wallet)

process_all_payments(payments, 1000)