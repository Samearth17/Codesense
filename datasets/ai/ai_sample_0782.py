class Character:
 def __init__(self, name, health=100):
 self.name = name
 self.health = health
 self.inventory = []

 def add_item(self, item):
 self.inventory.append(item)

 def remove_item(self, item):
 self.inventory.remove(item)

class Monster:
 def __init__(self, name, health=100, type="Monster"):
 self.name = name
 self.health = health
 self.type = type

 def attack(self, character):
 pass