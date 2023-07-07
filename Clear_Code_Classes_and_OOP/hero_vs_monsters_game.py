"""Hero vs Monsters game"""

class Monster:
    """Create Monster"""

    def __init__(self, damage, health, energy):
        self.damage = damage
        self.health = health
        self.energy = energy

    def __str__(self):
        return "Monster"

    def attack(self, someone):
        """create attack"""
        print("Monster attacks!")
        someone.get_damage(self.damage)
        self.energy = int(self.energy * 0.5)

    def get_damage(self, amount):
        """remove amount from health"""
        self.health -= amount

class Hero:
    """Create Hero"""

    def __init__(self, damage, health, energy):
        self.damage = damage
        self.health = health
        self.energy = energy

    def __str__(self):
        return "Hero"

    def attack(self, someone):
        """create attack"""
        print("Hero attacks!")
        someone.get_damage(self.damage)
        self.energy = int(self.energy * 0.5)

    def get_damage(self, amount):
        """remove amount from health"""
        self.health -= amount

class Scorpion(Monster):
    """Create scorpion"""
    def __init__(self, poison_damage, health, energy):
        super().__init__(damage=poison_damage, health=health, energy=energy)
        self.poison_damage = poison_damage

    def __str__(self):
        return "Scorpion"

    def attack(self, someone):
        """show poison damage"""
        someone.get_damage(self.poison_damage)
        self.energy = int(self.energy * 0.5)
        print(f"Scorpion dealt {self.poison_damage} poison damages to {someone}!")


# Create creatures
monster = Monster(damage=20, health=50, energy=20)

hero = Hero(damage=50, health=100, energy=50)

scorpion = Scorpion(poison_damage=80, health=70, energy=36)


# Print initial stats
print(f"Monster's stats are: health({monster.health}), energy({monster.energy})")
print(f"Hero's stats are: health({hero.health}), energy({hero.energy})")
print(f"Scorpion's stats are: health({scorpion.health}), energy({scorpion.energy})")

# Fight happens
hero.attack(monster)
monster.attack(hero)
hero.attack(scorpion)
scorpion.attack(hero)

# Print final stats
print(f"Monster's stats are: health({monster.health}), energy({monster.energy})")
print(f"Hero's stats are: health({hero.health}), energy({hero.energy})")
print(f"Scorpion's stats are: health({scorpion.health}), energy({scorpion.energy})")
