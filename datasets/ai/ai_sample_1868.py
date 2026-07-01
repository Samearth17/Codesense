import time
import random

questions = [...List of questions]

def start_game():
    score = 0
    start_time = time.time()
    for i in range( len(questions) ):
        print(f'Question {i+1}:')
        question = random.choice(questions)
        print(question['text'])
        print('Options:')
        for j, option in enumerate(question['options'], start=1):
            print(f"{j}. {option}")
        answer = int(input('Answer: '))
        if answer == question['answer']:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
        elapsed_time = time.time() - start_time
        print(f'Time remaining: {30 - int(elapsed_time):02} seconds\n')
        if elapsed_time >= 30:
            break
    print(f'Your score is {score}/{len(questions)}')

if __name__ == '__main__':
    start_game()