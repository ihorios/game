import random

class Map:
  red = "!"
  blue = "%"
  yellow = "#"
  violet = "@"
  green = "*"
  colors = [ "!", "%", "#", "@", "*" ];
  
  def __init__(self, height=5, width=5):
    self.height = height
    self.width = width
    self.map = []
    self.init()
    self.fill()  

  def getRandomColor(self):
    return random00.choice(self.colors);
    
  def init(self):
    for i in range(self.height):
      row = [];
      for j in range(self.width):
        row.append('')
      self.map.append(row)

  def __str__(self):
    string = ""
    for row in self.map:
      for item in row:
        string += item + " "
      string += "\n"
    return string

  def fill(self):
    i = 0
    for y in range(self.height):
      i = 0
      for x in range(self.width):
        self.map[y][x] = str(i);
        i += 1

  def getLeftGems(self, height, width):
    row = self.map[height]
    return row[0:width+1].reverse()

  def getRightGems(self, height, width):
    row = self.map[height]
    return row[width:len(row)]

  def getUpGems(self, height, width):
    col = []
    while(height >= 0):
      col.append(self.map[height][width])
      height -= 1
    return col

  def getDownGems(self, height, width)

    
    




























+
    

    










    
                                                                                                                                                                                 


 

  


        

