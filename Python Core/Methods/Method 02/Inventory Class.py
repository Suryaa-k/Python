# Q7. Build an Inventory class that:
# •	Tracks the total number of items across all inventories.
# •	Each instance maintains its own stock dictionary ({"item": quantity}).
# •	Provides a method to add or remove stock.
# •	Allows updating a minimum stock threshold globally.
# •	Offers a static checker to verify if a stock level is below threshold.

class Inventory:
    total_items = 0
    min_stock_threshold = 5

    def __init__(self, stock_dict):
        self.stock = stock_dict
        Inventory.total_items += sum(stock_dict.values())

    @staticmethod
    def is_below_threshold(quantity):
        stock_str = str(quantity)
        if stock_str[0] == '-':
            return False
        total = 0
        for char in stock_str:
            if char < '0' or char > '9':
                return False
            total = total * 10 + (ord(char) - ord('0'))
        return total < Inventory.min_stock_threshold

    def add_stock(self, item, quantity):
        stock_str = str(quantity)
        if stock_str[0] == '-':
            return False
        q = 0
        for char in stock_str:
            if char < '0' or char > '9':
                return False
            q = q * 10 + (ord(char) - ord('0'))
        if item in self.stock:
            self.stock[item] += q
        else:
            self.stock[item] = q
        Inventory.total_items += q
        return True

    def remove_stock(self, item, quantity):
        stock_str = str(quantity)
        if stock_str[0] == '-':
            return False
        q = 0
        for char in stock_str:
            if char < '0' or char > '9':
                return False
            q = q * 10 + (ord(char) - ord('0'))
        if item in self.stock and self.stock[item] >= q:
            self.stock[item] -= q
            Inventory.total_items -= q
            return True
        return False

    @classmethod
    def update_threshold(cls, new_threshold):
        if new_threshold >= 0:
            cls.min_stock_threshold = new_threshold

store1 = Inventory({"Rice": 10, "Wheat": 8})
store2 = Inventory({"Oil": 3, "Sugar": 12})

print("Total items:", Inventory.total_items)
print("Store1 stock:", store1.stock)
print("Store2 stock:", store2.stock)
print()
store1.add_stock("Milk", 5)
print("After adding Milk:", store1.stock)
print("New total items:", Inventory.total_items)

store2.remove_stock("Oil", 2)
print("After removing Oil:", store2.stock)
print()
print("Oil=3 below threshold?", Inventory.is_below_threshold(3))
print("Sugar=12 below threshold?", Inventory.is_below_threshold(12))
print()
Inventory.update_threshold(10)
print("New threshold:", Inventory.min_stock_threshold)
print("Sugar=12 below new threshold?", Inventory.is_below_threshold(12))
