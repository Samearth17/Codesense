import textwrap 

class TextGame(object):
    def __init__(self):
        self.level = 1
        self.is_playing = True

    def start_game(self):
        self.print_intro()
        while self.is_playing:
            self.level_one()

    def print_intro(self):
        # Introduction text
        intro = textwrap.dedent('''
            You awaken in a strange place, and it seems you have no memory of how you got there.
            You can feel cold dampness of the stone walls and ground beneath your feet.
            It appears to be a dungeon of some sort. You can see a light ahead. You decide to move
            towards it.
        ''')
        print(intro)

    def level_one(self):
        # Level one text
        level_one = textwrap.dedent('''
            As you make your way towards the light, you come across a fork in the path.
            You hear a soft whisper coming from the left path.
        ''')
        print(level_one)

        action = raw_input('''Do you choose to take the left or right path? ''')
        if action.upper() == "LEFT":
            self.level_two_left()
        elif action.upper() == "RIGHT":
            self.level_two_right()
        else:
            self.level_one()

    def level_two_left(self):
        # Level two left text
        level_two_left = textwrap.dedent('''
            The whisper gets louder as you take the left path. Eventually, you reach a small room.
            In the center of the room is a hooded figure standing in front of a pedestal.
            There is a strange looking artifact on the pedestal.
        ''')
        print(level_two_left)

        action = raw_input('''Do you 'approach' the figure or 'flee'? ''')
        if action.upper() == "APPROACH":
            print("You approach the figure and it removes its hood to reveal a face you recognize")
        elif action.upper() == "FLEE":
            print("You turn and run, taking the right path")
            self.level_two_right()
        else:
            self.level_two_left()

# Create instance and start the game. 
game = TextGame()
game.start_game()