# Q10. Create a class Member that:
# •	Has a shared BMI limit for “fit” status.
# •	Each member stores name, height, weight.
# •	Has a method to calculate BMI and check fit status.
# •	Provides a function to update BMI limit for all members.
# •	Offers a tool to check if height and weight entered are valid numbers.

class Member:
    
    bmi_limit = 24.9

    def __init__(self, name, height_m, weight_kg):
       
        self.name = name
        self.height_m = height_m
        self.weight_kg = weight_kg

    @staticmethod
    def is_valid_number(value):
        try:
            num = float(value)
            return num > 0
        except ValueError:
            return False

    def calculate_bmi(self):
        return self.weight_kg / (self.height_m ** 2)

    def is_fit(self):
        bmi = self.calculate_bmi()
        return bmi <= Member.bmi_limit

    @classmethod
    def update_bmi_limit(cls, new_limit):
        cls.bmi_limit = new_limit

m1 = Member("Rahul", 1.75, 70)     
m2 = Member("Priya", 1.60, 65)      
m3 = Member("Amit", 1.80, 85)

print("\n📊 INITIAL STATUS (BMI limit = 24.9):")
print(f"{m1.name:8} BMI:{m1.calculate_bmi():6.2f} {'FIT' if m1.is_fit() else 'NOT FIT'}")
print(f"{m2.name:8} BMI:{m2.calculate_bmi():6.2f} {'FIT' if m2.is_fit() else 'NOT FIT'}")
print(f"{m3.name:8} BMI:{m3.calculate_bmi():6.2f} {'FIT' if m3.is_fit() else 'NOT FIT'}")

# UPDATE SHARED BMI LIMIT (affects ALL objects)
print("\n🔄 Updating BMI limit to 25.0 for all members...")
Member.update_bmi_limit(25.0)
print(f"New shared BMI limit: {Member.bmi_limit}")

print("\n📊 NEW STATUS (BMI limit = 25.0):")
print(f"{m1.name:8} BMI:{m1.calculate_bmi():6.2f} {'FIT' if m1.is_fit() else 'NOT FIT'}")
print(f"{m2.name:8} BMI:{m2.calculate_bmi():6.2f} {'FIT' if m2.is_fit() else 'NOT FIT'}")
print(f"{m3.name:8} BMI:{m3.calculate_bmi():6.2f} {'FIT' if m3.is_fit() else 'NOT FIT'}")
