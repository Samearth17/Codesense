# Create the states
state0 = {
     'name': 'state0',
     'message': 'Hello! How can I help you?',
     'replies': {'I need some advice': 'state1', 'Can you answer my questions?': 'state2'}
}

state1 = {
     'name': 'state1',
     'message': 'Sure, what kind of advice do you need?',
     'replies': {'Career advice': 'state3','Health advice': 'state4'}
}

state2 = {
     'name': 'state2',
     'message': 'Yes, I'll do my best! What do you want to know?',
     'replies': {'Where can I find good tutorials': 'state5', 'Why is coding so hard': 'state6'}
}

state3 = {
     'name': 'state3',
     'message': 'It is always a good idea to research the field you are interested in and creating a plan to learn the skills that are required. Make sure to contact professionals in the field to understand their experience.',
     'replies': {}
}

state4 = {
     'name': 'state4',
     'message': 'Focus on eating healthy and staying active. Make sure to consult a medical professional if you have any concerns.',
     'replies': {}
}

state5 = {
     'name': 'state5',
     'message': 'You can find tutorials online or join coding communities to get help from experienced coders. StackOverflow and Cod Academy are great resources.',
     'replies': {}
}

state6 = {
     'name': 'state6',
     'message': 'Coding can be challenging, especially at first. Just remember that with practice, patience and problem solving skills you can overcome the obstacles.',
     'replies': {}
}


# Initialize the state
current_state = state0

# Keep a record of conversation
conversation = []

while True:
 # Print the current state message
 print(current_state['message'])
 conversation.append(current_state['message'])

 # Get the user input
 user_input = input('>> ')
 conversation.append(user_input)

 # Update the state
 if user_input in current_state['replies']:
  current_state = eval(current_state['replies'][user_input])
 else:
  print("I don't understand what you mean. Please try again.")

# End the conversation when the state is terminal
 if not bool(current_state['replies']):
  print('Goodbye!')
  break

print("=========================")
print("Conversation:")
for message in conversation:
 print(message)