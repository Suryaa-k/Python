# • Create a class PasswordValidator with a method validate(password). Raise an 
# exception if the password length is less than 8 characters.

class PasswordValidator:
    def validate(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        print("Password is valid")


# --- main code ---
try:
    pwd = input("Enter password: ")
    validator = PasswordValidator()
    validator.validate(pwd)
except ValueError as e:
    print("Error:", e)
