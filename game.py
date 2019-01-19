# Simple game

import sys
import os
from hero_common import HeroCommon
from hero_uncommon import HeroUncommon
from map import Map

def pause():
  if sys.version_info < (3, 4):
    raw_input()
  else:
    input()

os.system('color 0')

jane = HeroCommon("Jane")
olaf = HeroUncommon("Olaf")


print(" ");
os.system('color 1')
print("-------------------------");
os.system('color 2')
print("--- WELCOME TO HEROES ---");
os.system('color 3')
print("-------------------------");
print(" ");
mapp = Map(5, 7)
print(mapp);
print(" ");
print (jane.toString())
print (olaf.toString())
os.system('color 0')
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
   
