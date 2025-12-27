# • Create a class Transaction with a method process() that uses try, except, and 
# finally blocks to ensure a cleanup message is always printed.

class Transaction:
    def process(self, balance, amount):
        try:
            print("Starting transaction...")
            if amount > balance:
                raise ValueError("Insufficient balance for this transaction")
            balance -= amount
            print("Transaction successful. Remaining balance:", balance)
        except ValueError as e:
            print("Transaction failed:", e)
        finally:
            
            print("Cleaning up transaction resources...\n")

t = Transaction()
t.process(500, 1000)  
t.process(1500, 1000)  
