import turtle
# task 1

games = ["Монополія", 'Шахи', 'Твістер']
foods = ["Піцца", 'Спагетті', "Спартак"]
favorites = games + foods
print(favorites)

# task 2
res1 = (25 * 3) + (40 * 2)
res2 = 25 * 3 + 40 * 2
print(res1)
print (res2)

# task 3
# https://www.programiz.com/python-programming/string-interpolation
myName = 'Ihor'
myLastName= 'Osadchyi'
message = 'Hello, %s %s'
print(message %(myName, myLastName))

# lesson2
# task 1
t = turtle.Pen()
t.forward(50)
t.left(90) 
t.forward(100)
t.left(90)
t.forward(50)
t.left(90) 
t.forward(100)
t.clear()

# task 2
t = turtle.Pen()
t.forward(30)
t.left(615)
t.forward(50)
t.left(215)
t.forward(50)
t.clear()

# task 3
t = turtle.Pen()
t.forward(50)
t.up()
t.forward(50)
t.left(90)
t.forward(50)
t.down()
t.forward(50)
t.up()
t.forward(50)
t.left(90)
t.forward(50)
t.down()
t.forward(50)
t.up()
t.forward(50)
t.left(90)
t.up()
t.forward(50)
t.down()
t.forward(50)
t.clear()
input()
