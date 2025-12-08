from abc import ABC, abstractmethod
class AlertService (ABC):
    def __init__(self,name,passw):
        self.__name=name
        self.__passw=passw 
        self.l=[]
    @abstractmethod
    def trigger():
        pass

    def getName(self):
        return self.__name
    
    def getpassw(self):
        return self.__passw
    
    def __add__(self,obj):
        self.l.append(obj)

    def config(self):
        print("Config Done")

class SMSAlert(AlertService):
    def trigger(self):
        print("SMS Sent")

class AppAlert(AlertService):
    def trigger(self):
        print("App Alert Sent")

class EMailAlert(AlertService):
    def trigger(self):
        print("Email Alert Sent")

def service_manager(obj):
    obj.trigger()