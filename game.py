# Simple game

import sys
from armor import Armor

def pause():
  if sys.version_info >= (3, 5):
    raw_input()
  else:
    input()

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

jane = HeroCommon("Jane")
olaf = HeroUncommon("Olaf")
print (jane.toString())
print (olaf.toString())

count = 0
while jane.hp > 0 and olaf.hp > 0:
  count += 1
  print ("Attack " + str(count))
  if jane.hp > 0:
    damage = jane.attack()
    damage = olaf.armor.protect(damage)
    olaf.hp = olaf.hp - damage
    print ("Jane attack:" + olaf.toString())
  if olaf.hp > 0:
    damage = olaf.attack()
    damage = jane.armor.protect(damage)
    jane.hp = jane.hp - damage
    print ("Olaf attack:" + jane.toString())
  pause()
if jane.hp > 0:
   print ("Winner: " + jane.toString())
if olaf.hp > 0:
   print ("Winner: " + olaf.toString())
   
