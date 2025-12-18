# Q5. Using the abc module, create an abstract class Notification with send().
# Implement subclasses EmailNotification, SMSNotification, PushNotification — each
# with its own send() logic.
# Demonstrate polymorphism by looping over all and calling send().

class Notification:
    def send(self):
        print("Just a Message")

class Email(Notification):
    def send(self):
        print("Notification Email")

class SMS(Notification):
    def send(self):
        print("Notification SMS")

class Push(Notification):
    def send(self):
        print("Notification Push")


obj = Email()
obj1 = SMS()
obj2 = Push()
li = [obj,obj1,obj2]
for i in li:
    i.send()
