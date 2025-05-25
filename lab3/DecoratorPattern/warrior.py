from abc import ABC, abstractmethod

# Component
class Warrior(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

# Concrete Component
class BasicWarrior(Warrior):
    def attack(self) -> str:
        return "ataca con sus puños"

# Decorator
class WarriorDecorator(Warrior):
    def __init__(self, warrior: Warrior):
        self._warrior = warrior
    
    def attack(self) -> str:
        return self._warrior.attack()

# Concrete Decorator 1
class SwordDecorator(WarriorDecorator):
    def attack(self):
        return f"{ self._warrior.attack()} y con una espada"

# Concrete Decorator 2
class ArmorDecorator(WarriorDecorator):
    def attack(self):
        return f"{ self._warrior.attack()} mientras está protegido con una armadura mágica"

# Concrete Decorator 3
class FireDecorator(WarriorDecorator):
    def attack(self):
        return f"{ self._warrior.attack()} con el fuego infernal"


if __name__ == "__main__":
    warrior = BasicWarrior()
    print("Guerrero básico:", warrior.attack())

    warriorWithSword = SwordDecorator(warrior)
    print("Guerrero con espada:", warriorWithSword.attack())

    warriorWithArmor = ArmorDecorator(warriorWithSword)
    print("Guerrero con espada y armadura:", warriorWithArmor.attack())

    warriorFullEquiped = FireDecorator(warriorWithArmor)
    print("Guerrero al máximo:", warriorFullEquiped.attack())