# - *- coding: utf-8 - *-
import random
print("Вітаємо вас в Вгадайці")
print("\n")
ans = random.randint(0, 100)
print("Я загадав число від 0 до 100 попробуй його відгадати:")
trying = int(input("Твоя здогадка:"))
while trying != ans:
  if trying > ans:
    print("Число меншe")
    trying = int(input("Твоя здогадка:"))
  elif trying < ans: 
    print("Число більше")
    trying = int(input("Твоя здогадка:"))
print("Та,ти вгадав це число " + str(ans) + " !")
         
