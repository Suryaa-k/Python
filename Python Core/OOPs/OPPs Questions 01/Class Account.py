# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.

class Account:
    def withDraw(self):
        print("Withdrawing Amount")

class SavingAcc(Account):
    def withDraw(self):
        super().withDraw()
        print("Withdrawing Saving Amount")

class PremiumSavingAcc(SavingAcc):
    def withDraw(self):
        super().withDraw()
        print("Withdrawing Premium Saving Amount")

obj = PremiumSavingAcc()
obj1 = SavingAcc()
obj.withDraw()