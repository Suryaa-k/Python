# • Create a class LoginSystem with a method login(password) that raises an 
# exception for an incorrect password and handles the exception outside the class.

class LoginSystem:
    def __init__(self, correct_password):
        self.correct_password = correct_password

    def login(self, password):
        if password != self.correct_password:
        
            raise ValueError("Incorrect password")
        print("Login successful!")

system = LoginSystem("python123")

try:
    pwd = input("Enter password: ")
    system.login(pwd)
except ValueError as e:
    print("Login failed:", e)
