import random

def computer_guess(n):
    low = 1
    high = n
    result = ''
    while result != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        result = input(f'If {guess} is too hig (H), too low (L), or correct (C) ?').lower()
        if result == 'h':
            high = guess - 1
        elif result == 'l':
            low = guess + 1

    print(f'The computer guessed the number,{guess}, correctly!')


computer_guess(10)


