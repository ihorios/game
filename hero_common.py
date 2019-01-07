from armor import Armor
class HeroCommon:
  def __init__(self, name):
    self.name = name
    self.hp = 90
    self.armor = Armor()
    self.stars = 1
  def attack(self):
    return 50 

  def toString(self):
    return self.name + ":" + str(self.hp) + self.armor.toString()
 
