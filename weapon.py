import random
class Weapon:
  types = ["sword", "axe", "knife", "spear", "mace", "bow"]
  def __init__(self):
    self.name = random.choice(self.types)
    self.damage = random.randint(1, 50)

  def toString(self):
    return self.name + ":" + str(self.damage)

  def attack(self):
    return self.damage      
