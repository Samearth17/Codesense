class Fibonacci:
 def __init__(self, n):
  self.n = n
  self.a = 0
  self.b = 1
 
 def __iter__(self): 
  return self
 
 def __next__(self): 
  if self.a <= self.n:
   temp = self.a
   self.a, self.b = self.b, self.a + self.b 
   return temp 
  else:
  raise StopIteration