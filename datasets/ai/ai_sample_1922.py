# Define menu
menu = ['Calculator', 'Quiz', 'Message Board', 'Live Chat']

# Print menu
print("Menu:")
for item in menu:
  print("-", item)

# Run a loop until user quits the program
done = False
while not done:
  # Print list of options
  selection = input("Type the name of the action you want to select (or type 'Quit to exit): ")
  if selection == 'Calculator':
    # Code for Calculator
    print("Calculator....")
  elif selection == 'Quiz':
    # Code for Quiz
    print("Quiz....")
  elif selection == 'Message Board':
    # Code for Message Board
    print("Message Board....")
  elif selection == 'Live Chat':
    # Code for Live Chat
    print("Live Chat....")
  elif selection == 'Quit':
    done = True
  else:
    print("Invalid selection, please choose from the list of options.")