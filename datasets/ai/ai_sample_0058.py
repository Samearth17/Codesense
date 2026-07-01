class StringComparator:

def __init__(self, string1, string2):
 self.string1 = string1
 self.string2 = string2

def is_equal(self):
 return self.string1 == self.string2

def is_different(self):
 return self.string1 != self.string2

def is_similar(self, threshold=0.5):
 distance = edit_distance(self.string1, self.string2)
 max_length = max(len(self.string1), len(self.string2))

 return distance / max_length < threshold