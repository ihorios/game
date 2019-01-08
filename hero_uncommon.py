from armor import Armor
from weapon import Weapon
class HeroUncommon:
  def __init__(self, name):
    self.name = name
    self.hp = 105
    self.armor = Armor()
    self.stars = 2
    self.weapon = Weapon()

  def attack(self):
    return self.weapon.attack()

  def defend(self, damage):
    damage = self.armor.protect(damage)
    self.hp = self.hp - damage
    return self.isAlive()

  def toString(self):
    return self.name + ":" + str(self.hp) + self.armor.toString() + self.weapon.toString()

  def isAlive(self):
    if self.hp < 0:
      self.hp = 0
    return self.hp > 0 
