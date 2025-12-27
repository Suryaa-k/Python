# • Create a class BankAccount with an attribute balance. Implement a method 
# withdraw(amount) that raises an exception if the withdrawal amount is greater 
# than the available balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # starting balance

    def withdraw(self, amount):
        if amount > self.balance:
            # raise an exception if not enough money
            raise ValueError("Withdrawal amount exceeds available balance")
        self.balance -= amount
        print("Withdrawal successful. New balance:", self.balance)


# --- example usage ---
try:
    account = BankAccount(500)
    amt = int(input("Enter amount to withdraw: "))
    account.withdraw(amt)
except ValueError as e:
    print("Error:", e)
