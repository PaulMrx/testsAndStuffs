"""Monster class exercise 02"""

class Monster:
    """Create monster class"""

    def __init__(self, num, func):
        print("Monster created")
        self.num = num
        self.func = func

class Attacks:
    """Create attacks class"""

    def __init__(self, num):
        print("Attacks created")
        self.num = 

    def bite(self, num):
        """bite function"""
        print(f"Monster{num} has bitten")

    def strike(self, num):
        """strike function"""
        print(f"Monster{num} has stroke")

    def slash(self, num):
        """slash function"""
        print(f"Monster{num} has slashed")

    def kick(self, num):
        """kick function"""
        print(f"Monster{num} has kicked")


monster1 = Monster(num = 1, func = Attacks().kick)
monster2 = Monster(num = 2, func = Attacks().bite)

monster1.func(1)
monster2.func(2)


