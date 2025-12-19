# Create a custom exception named InvalidAgeError. Create a class Voter with a 
# method check_eligibility(age) that raises this exception if age is less than 18.

# Custom exception
class InvalidAgeError(Exception):
    def __init__(self, age, message):
        self.age = age
        self.message = message
        super().__init__(f" Given age: {age}. {message}")


class Voter:
    def check_eligibility(self, age):
        # 1) Negative age → custom exception
        if age < 0:
            raise InvalidAgeError(age, "Age cannot be negative")

        # 2) Below 18 → not eligible
        if age < 18:
            print("Not eligible to vote")

        # 3) 18 or above → eligible
        else:
            print("Eligible to vote")


# --- main code ---
try:
    age = int(input("Enter your age: "))
    v = Voter()
    v.check_eligibility(age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid integer age")


