class Monster:
    # Monster class
    def __init__(self, number, health, energy, speed):
        self.number = number
        self.health = health
        self.energy = energy
        self.speed = speed

    def __str__(self):
        return f"I am Monster {self.number}"
    
    def attack(self, amount=0):
        # Attacking another object
        print("The Monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        print(f"Monster's energy down to {self.energy}")

    def move(self):
        # Move this object
        print(f"Monster has moved by {self.speed}")

monster = Monster(5, 90, 50, 50)
print(monster)
