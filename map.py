class Map:
  def __init__(self, height=3, width=3):
    self.height = height
    self.width = width
    self.map = []
    self.fill()

  def fill(self):
    for i in range(self.height):
      row = [];
      for j in range(self.width):
        row.append("X") 
      self.map.append(row)

  def __str__(self):
    string = ""
    for row in self.map:
      for item in row:
        string += item
      string += "\n"
    return string

