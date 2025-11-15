# Q6. Design a class Vehicle that:
# •	Keeps a record of service charge rate common to all vehicles.
# •	Each vehicle has a model, kilometers_run, and service history.
# •	Has a function to calculate service charge based on km and rate.
# •	Provides a method to update the service rate for all vehicles.
# •	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
from sys import exception


class Vehicle:
    service_charge=1500

    def __init__(self, model, km, history):
        self.model = model
        self.km = km
        self.history = history

    def charge(self):
        if self.veh_reg(self.history):
             print(self.km*(3/10)+self.service_charge)
        else:
            print("Not Eligible For Service")

    @classmethod
    def update_rate(cls,new_charge):
        cls.service_charge= new_charge

    @staticmethod
    def veh_reg(year):
        if year < 15:
            return True
        else:
            return False

obj1 = Vehicle("Pulsar", 15000, 16)
obj2=Vehicle("Pulsar", 150, 2)
obj2.charge()
obj1.charge()




