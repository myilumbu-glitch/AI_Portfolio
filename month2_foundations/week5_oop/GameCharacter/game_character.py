# (03.03.26) Game Character Class

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50

    def take_damage(self, amount):
        self.health -= amount
        print(f"Took {amount} damage")
        if self.health <= 0:
            print("Hero has fallen!")

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"Healed {amount}, current health: {self.health}")

    def cast_spell(self, cost):
        if self.mana < cost:
            print("Not enough mana to cast the spell")
        else:
            self.mana -= cost
            print(f"Casted spell costing {cost} mana")

    def restore(self):
        self.mana += 10
        print("Restored 10 mana")

    def status(self):
        print(f"Health: {self.health}, Mana: {self.mana}")


# Test
hero1 = Hero("King")

hero1.status()
hero1.take_damage(30)
hero1.status()
hero1.heal(20)
hero1.cast_spell(40)
hero1.status()
hero1.cast_spell(20)
hero1.restore()
hero1.status()
hero1.take_damage(120)
