# Q4. Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).

class Loan:
    common_intrest=10
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def total_amount(self):
        return self.principal + (self.principal * self.common_intrest)/100
    @classmethod
    def update_intrest(cls,new_intrest):
        cls.common_intrest = new_intrest
    @staticmethod
    def loan_verify(loan):
        salary=int(input("Enter your salary: "))
        if loan.principal<salary*20 :
            print ("You are eligible for loan")
            print(f"Your loan amount is: {Loan.total_amount(obj1)}")
        else:
            print("You are not eligible for loan")
obj1=Loan("John",100000)
obj1.update_intrest(5)
obj1.loan_verify(obj1)


