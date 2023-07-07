"""Module for Monster class"""

class Monster:
    """Monster class"""

    def __init__(self, number, health=100, energy=50, speed=40):
        self.number = number
        self.health = health
        self.energy = energy
        self.speed = speed

    def __str__(self):
        return f"I am Monster {self.number}"

    def attack(self, amount=0):
        """Attack object"""
        print("The Monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        print(f"Monster's energy down to {self.energy}")

    def move(self):
        """Move object"""
        print(f"Monster has moved by {self.speed}")

monster1 = Monster(1)
monster2 = Monster(2)
print(monster1.health)
print(monster2.health)
