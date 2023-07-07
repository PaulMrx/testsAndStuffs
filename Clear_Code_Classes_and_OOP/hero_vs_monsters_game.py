"""Hero vs Monsters game"""

class Hero:
    """Create generic hero"""

    def __init__(self, damage, health, energy):
        self.damage = damage
        self.health = health
        self.energy = energy

    def __str__(self):
        return f"{__class__.__name__}"

    def attack(self, someone):
        """Deals simple damage and reduces energy"""
        print(f"Hero attacks and deals {self.damage} to {someone}!")
        someone.get_damage(self.damage)
        self.energy = int(self.energy * 0.5)

    def get_damage(self, amount):
        """remove amount from health"""
        self.health -= amount


class Monster:
    """Create generic monster"""

    def __init__(self, damage, health, energy):
        self.damage = damage
        self.health = health
        self.energy = energy

    def __str__(self):
        return f"{__class__.__name__}"

    def attack(self, someone):
        """Deals simple damage and reduces energy"""
        print(f"Monster attacks and deals {self.damage} to {someone}!")
        someone.get_damage(self.damage)
        self.energy = int(self.energy * 0.5)

    def get_damage(self, amount):
        """remove amount from health"""
        self.health -= amount


class Scorpion(Monster):
    """Create scorpion monster"""

    def __init__(self, poison_damage, health, energy):
        super().__init__(damage=poison_damage, health=health, energy=energy)
        self.poison_damage = poison_damage

    def __str__(self):
        return f"{__class__.__name__}"

    def attack(self, someone):
        """Deals poison damage instead of simple damage and reduces energy"""
        someone.get_damage(self.poison_damage)
        self.energy = int(self.energy * 0.5)
        print(f"Scorpion attacks and deals {self.poison_damage} poison damages to {someone}!")


# Create creatures
monster = Monster(damage=20, health=50, energy=20)

hero = Hero(damage=50, health=100, energy=50)

scorpion = Scorpion(poison_damage=80, health=70, energy=36)


# Print initial stats
print(f"Monster's stats are: health({monster.health}), energy({monster.energy})")
print(f"Hero's stats are: health({hero.health}), energy({hero.energy})")
print(f"Scorpion's stats are: health({scorpion.health}), energy({scorpion.energy})")
print("")

# Make them fight
hero.attack(monster)
monster.attack(hero)
hero.attack(scorpion)
scorpion.attack(hero)
print("")

# Print final stats
print(f"Monster's stats are: health({monster.health}), energy({monster.energy})")
print(f"Hero's stats are: health({hero.health}), energy({hero.energy})")
print(f"Scorpion's stats are: health({scorpion.health}), energy({scorpion.energy})")

# print("")
# help(Scorpion)
