class Vector2D:
 def __init__(self, x = 0, y = 0):
  self.x = x
  self.y = y

def __str__(self):
 return '<' + str(self.x) + ', ' + str(self.y) + '>'

def add(self, other):
 return Vector2D(self.x + other.x, self.y + other.y)

def __add__(self, other):
 return self.add(other)

# testing
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(v1 + v2)

# Output: <4, 6>