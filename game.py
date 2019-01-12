# Simple game

import sys
from hero_common import HeroCommon
from hero_uncommon import HeroUncommon
from map import Map

def pause():
  if sys.version_info < (3, 4):
    raw_input()
  else:
    input()




jane = HeroCommon("Jane")
olaf = HeroUncommon("Olaf")
print(" ");
print("-------------------------");
print("--- WELCOME TO HEROES ---");
print("-------------------------");
print(" ");
mapp = Map()
print(mapp);
print(" ");
print (jane.toString())
print (olaf.toString())

count = 0
while jane.hp > 0 and olaf.hp > 0:
  count += 1
  print ("Attack " + str(count))
  if jane.isAlive():
    olaf.defend(jane.attack())
    print ("Jane attack:" + olaf.toString())
  if olaf.isAlive():
    jane.defend(olaf.attack())
    print ("Olaf attack:" + jane.toString())
  pause()
if jane.hp > 0:
   print ("Winner: " + jane.toString())
if olaf.hp > 0:
   print ("Winner: " + olaf.toString())
   
