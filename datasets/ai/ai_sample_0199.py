# Player class
class Player(object):
 def __init__(self):
 self.health = 100
 self.location = 'room one'
 self.monsters_killed = 0

# Room class
class Room(object):
 def __init__(self):
 self.name = ''
 self.description = ''
 self.monsters = []

 def add_monster(self, monster):
 self.monsters.append(monster)

# Monster class
class Monster(object):
 def __init__(self):
 self.name = ''
 self.health = 100

 def attack(self, player):
 player.health -= 10

# Function to start the game
def start_game():
 # Create player, rooms and monsters
 player = Player()

# Main game loop
while True:
 # Show the current room;
 print(f'You are in {player.location}.')
 # Display available actions
 print('Available actions: move, fight')
 # Get user's action
 response = input('What would you like to do? ').lower()

 # Moving to a new room
 if response == 'move':
 # Get the list of available rooms
 # Get the user's destination
 # Move the player to the chosen room

# Fighting a monster
 if response == 'fight':
 # Get all monsters in the current room
 # Get the user's chosen monster
 # Initiate a battle between the player and the monster

# End of the game
 if player.health <= 0:
 print ('You have been defeated!')
 break

if __name__ == '__main__':
 start_game()