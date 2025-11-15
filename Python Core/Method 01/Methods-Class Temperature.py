# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
    def show_conversion(self):
        print("The celsius is",self.celsius)
        print("The fahrenheit is",self.to_fahrenheit(self.celsius))
obj = Temperature(int(input("The Celsius is: ")))
obj.show_conversion()