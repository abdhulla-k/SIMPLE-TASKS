import random

def guess(x):
    random_number = random.randint(1, x)
    
    guess = 0

    while random_number != guess:
        guess = int(input(f'guess a bumber between 1 and {x}:'))
        if guess < random_number :
            print('sorry, guess again.Too low.')
            
        elif guess > random_number :
            print('sorry, guess again.Too hig')
            
    print(f'congrats. You have guessed the numbor {random_number} correctly!')

guess(10)