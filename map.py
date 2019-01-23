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

  def getRandomGem(self):
    return random.choice(self.colors);
    
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
    for y in range(self.height):
      for x in range(self.width):
        self.map[y][x] = self.rules(y, x)

  def getLeftGems(self, height, width):
    row = self.map[height]
    result = row[0:width+1]
    result.reverse()
    return result

  def getRightGems(self, height, width):
    row = self.map[height]
    return row[width:len(row)]

  def getUpGems(self, height, width):
    col = []
    while(height >= 0):
      col.append(self.map[height][width])
      height -= 1
    return col

  def getDownGems(self, height, width):
    col = []
    while(height < self.height):
      col.append(self.map[height][width])
      height += 1
    return col

  def explodeGems(self, gems):
    if len(gems) < 3:
      return 0;
    if gems[0] == gems[1] and gems[0] == gems[2]:
      return 1;
    else:
      return 0;

  def rules(self, height, width):
    candidate = self.getRandomGem()
    leftGems = self.getLeftGems(height, width)
    upGems = self.getUpGems(height, width)
    leftGems[0] = candidate
    upGems[0] = candidate
    while self.explodeGems(leftGems) or self.explodeGems(upGems):
      candidate = self.getRandomGem()
      leftGems = self.getLeftGems(height, width)
      upGems = self.getUpGems(height, width)
      leftGems[0] = candidate
      upGems[0] = candidate
    return candidate
                                                                                                                


  


        

