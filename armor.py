import random
class Armor:
  types = ["armory", "helmet", "shield", "mail"]  
  def __init__(self):
    self.name = random.choice(self.types)
    self.defence = random.randint(1, 20)

  def toString(self):
    return self.name + ":" + str(self.defence)  

  def protect(self, damage):
    if damage < self.defence:
      return 0
    return damage - self.defence      
    
