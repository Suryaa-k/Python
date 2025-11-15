class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def change_bank(self,new_account):
        self.bank_name=new_account
    @staticmethod
    def validate_amount(x):
        return x>0
b1=BankAccount("Surya",5000)
b2=BankAccount("Lokesh",1300)
b3=BankAccount("Shiva",2500)
b1.deposit(1000)
b2.deposit(3000)
b1.change_bank("HDFC")
print(b1.bank_name)
print(b2.bank_name)
print(b3.bank_name)

