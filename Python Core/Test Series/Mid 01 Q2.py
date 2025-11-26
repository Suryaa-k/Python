# 2.	Design:
# • Abstract base class Sensor with functions read_value() and calibrate()
# • Subclasses: TemperatureSensor, PressureSensor, HumiditySensor
# Encapsulate:
# • internal raw sensor readings – print something which indicates type of sensor
# • calibration factor – log something which indicateds “calibration done successfully”
# Hide all raw operations and allow only a public, clean get_reading() method.

from abc import ABC, abstractmethod
class Sensor(ABC):
    @abstractmethod
    def read_value():
        pass
    @abstractmethod
    def calibrate():
        pass
class TS(Sensor):
    def __read_value(self):
        print("TS")
    
class HS(Sensor):
    def __read_value(self):
        print("HS")

class PS(Sensor):
    def __read_value(self):
        print("PS")

def get_reading(self):
    self.__read_value()


