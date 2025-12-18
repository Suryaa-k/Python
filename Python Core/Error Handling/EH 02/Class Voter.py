# Create a custom exception named InvalidAgeError. Create a class Voter with a 
# method check_eligibility(age) that raises this exception if age is less than 18.

class Voter(Exception):
    def __init__(self,n,msg):
        self.name=n
        self.message=msg 
raise Voter("Surya",16)
