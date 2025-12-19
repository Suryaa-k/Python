# • Create a class UserInput with a method get_integer(value). Handle ValueError 
# and TypeError using separate except blocks.

class UserInput:
    def get_integer(self, value):
        try:
            num = int(value)
            print("You entered integer:", num)
            return num
        except ValueError:
            print("ValueError: The given value cannot be converted to an integer.")
        except TypeError:
            print("TypeError: The given input type is not valid for integer conversion.")

ui = UserInput()

v1 = input("Enter first value: ")
ui.get_integer(v1)



