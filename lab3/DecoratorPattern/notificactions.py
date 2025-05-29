from abc import ABC, abstractmethod

# Component
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Concrete Component
class BaseNotifier(Notifier):
    def send(self, message: str):
        print(f"Basic notification: {message}")

# Decorator
class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str):
        self._wrapped.send(message)

# Decorator 1: Email
class EmailNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"Sending via Email: {message}")

# Decorator 2: SMS
class SMSNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"Sending via SMS: {message}")



if __name__ == "__main__":
    # Compose notifications: Base → Email → SMS
    notifier = SMSNotifier(
                   EmailNotifier(
                       BaseNotifier()
                   )
               )

    notifier.send("Hola, ¿todo bien?")