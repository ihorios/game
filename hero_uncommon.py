from armor import Armor
class HeroUncommon:
  def __init__(self, name):
    self.name = name
    self.hp = 105
    self.armor = Armor()
    self.stars = 2

  def attack(self):
    return 60

  def toString(self):
    return self.name + ":" + str(self.hp) + self.armor.toString()
