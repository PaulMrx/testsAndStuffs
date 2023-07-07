"""Hero vs Monsters game"""

class Monster:
    """Create Monster"""

    def __init__(self, damage, health, energy):
        self.damage = damage
        self.health = health
        self.energy = energy

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
    def __init__(self, damage, health, energy, poison_damage):
        super().__init__(damage, health, energy)
        self.poison_damage = poison_damage

    def attack(self):
        """show poison damage"""
        print(f"Scorpion dealt {self.poison_damage} poison damages!")



monster = Monster(20, 50, 20)
hero = Hero(50, 100, 50)
scorpion = Scorpion(30, 70, 36, 80)



print(f"Monster's stats are: health({monster.health}), energy({monster.energy})")
print(f"Hero's stats are: health({hero.health}), energy({hero.energy})")

hero.attack(monster)
monster.attack(hero)
scorpion.attack()

print(f"Monster's stats are: health({monster.health}), energy({monster.energy})")
print(f"Hero's stats are: health({hero.health}), energy({hero.energy})")
