# You are building a notification system for a large-scale application such as a
# banking platform or an online learning portal.
# The system must support sending notifications through multiple channels such
# as email, SMS, and push notifications.

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def __init__(self):
        self.__api_key = "EMAIL_API_KEY_123"
    def send(self, message):
        print(f"Email Message: {message}")
        print()

class SMSNotifier(Notifier):
    def __init__(self):
        self.__api_key = "SMS_API_KEY_456"
    def send(self, message):
        print(f"SMS Message: {message}")
        print()

class PushNotifier(Notifier):
    def __init__(self):
        self.__api_key = "PUSH_API_KEY_789"
    def send(self, message):
        print(f"Push Message: {message}")
        print()

def notify_all(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)

email = EmailNotifier()
sms = SMSNotifier()
push = PushNotifier()

notifiers = (email, sms, push)

notify_all(notifiers, "System maintenance scheduled tonight.")



