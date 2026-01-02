# 7. Create a module containing two classes where one uses composition and another 
# uses inheritance to reuse code from a base class. Import and demonstrate the 
# difference between the two approaches.

class Baseclass:
    def display(self):
        print("BaseClass")

class inhertance(Baseclass):
    def display(self):
        super().display()
        print("Using inhertance")

class composition:
    def display(self):
        self.obj = Baseclass()
        self.obj.display()
        print("Using composition")