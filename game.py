# Simple game

import sys
from hero_common import HeroCommon
from hero_uncommon import HeroUncommon

def pause():
  if sys.version_info >= (3, 5):
    raw_input()
  else:
    input()




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
   
