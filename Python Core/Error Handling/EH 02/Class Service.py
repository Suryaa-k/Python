# • Create a class Service with a method that calls another method which raises an 
# exception. Catch and handle the exception in the Service class.

class Service:
    def __helper_operation(self, x, y):
  
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero inside helper_operation")
        return x / y

    def do_task(self, x, y):
        try:
            result = self.__helper_operation(x, y)
            print("Result:", result)
        except ZeroDivisionError as e:
            print("Handled in Service:", e)

s = Service()
s.do_task(10, 2)   
s.do_task(10, 0)   
