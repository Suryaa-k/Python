# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.

class UPI:
    def pay(self, amount):
        print(f"{amount} paid Using UPI")

class Card:
    def pay(self, type, Amount):
        print(f"{Amount} Amount paid Using {type} Card")

class Cash:
    def pay(self, amount):
        print(f"{amount} paid Using Cash")

def check(ob):
    if isinstance(ob, UPI):
        ob.pay(1000)
    elif isinstance(ob, Card):
        ob.pay("Credit", 10000)
    elif isinstance(ob, Cash):
        ob.pay(6000)
    else:
        print("Not UPI or Card or Cash")

l = Card()
k = Cash()
m = UPI()

check(l)
check(m)
check(k)