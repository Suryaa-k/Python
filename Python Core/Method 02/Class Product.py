# Q2. Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).

class Product:
    base_tax=8
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def update_price(self):
        return self.price + (self.price * self.base_tax)/100
    @classmethod
    def changed_tax(cls, new_tax):
        cls.base_tax = new_tax
    @staticmethod
    def value(price):
        if price<0:
            return "Not Valid"
        else:
            return price
obj1=Product("Python",30000)
print(obj1.price)
print(obj1.update_price())
Product.changed_tax(10)
print(obj1.update_price())






