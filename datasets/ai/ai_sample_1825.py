import random

def set_choice(user_choice):
    return user_choice

def generate_computer_choice():
    computer_choice = random.choice(['Rock', 'Paper', 'Scissor'])
    return computer_choice

def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('It is a tie!')
    elif user_choice == 'Rock':
        if computer_choice == 'Paper':
            print('You lose!')
        else:
            print('You win!')
    elif user_choice == 'Paper':
        if computer_choice == 'Scissor':
            print('You lose!')
        else:
            print('You win!') 
    elif user_choice == 'Scissor':
        if computer_choice == 'Rock':
            print('You lose!')
        else:
            print('You win!')
    else:
        print('Please enter a valid choice!')
            
if __name__ == '__main__':
    user_choice = input('Please enter your choice: ')
    user_choice = set_choice(user_choice)
    computer_choice = generate_computer_choice()
    print(f'Computer chose: {computer_choice}')
    compare_choices(user_choice, computer_choice)