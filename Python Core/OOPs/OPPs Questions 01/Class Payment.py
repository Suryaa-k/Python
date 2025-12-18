# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.

class Payment:
    def process(self, amount):
        print(f"{amount} Need to be paid")

class CreditCard(Payment):
    def process(self, amount, card_type):
        super().process(amount)
        print(f"will be paid using {card_type}")

obj = Payment()
obj1 = CreditCard()

def fun(obj):
    if isinstance(obj, CreditCard):
        obj1.process(100, "Cash")
    elif isinstance(obj, Payment):
        obj.process(600)
    else:
        print("No class")

fun(obj1)
fun(obj)