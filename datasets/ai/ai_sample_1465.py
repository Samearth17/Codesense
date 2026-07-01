class CompressedDataStructure():
 def __init__(self):
  self.data = {}

 def insert(self,key,value):
  self.data[key] = value

 def search(self,key):
  if key in self.data:
   return self.data[key]
  else:
   raise KeyError

 def delete(self,key):
  del self.data[key]