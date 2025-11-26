# 1.	Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal list)

class ShoppingCart:
    def __init__(self):
        self.__l=[]
    def add(self,item):
        self.__l.append(item)
    def remove(self,item):
        self.__l.remove(item)
    def get_list(self):
        return self.__l.copy()
sl=ShoppingCart()
sl.add("fruits")
sl.add("chocolates")
sl.remove("chocolates")
print(sl.get_list())