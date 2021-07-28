import random

def play():
    player = input("Enter 'r' for rock, 'p' for paper and 's' for scissors")
    computer = random.choice(['r','p','s']) # This code will be used to select one from the list bu the computer

    if player == computer :
        return 'it\'s a tie'
    
    if win(player, computer):
        return 'You won!'
    
    return 'You lost!'

def win(play, compu):
    # return True if player wins
    # r > s, s > p, p > r
    if (play == 'r' and compu == 's') or (play == 's' and compu == 'p') \
        or (play == 'p' and compu == 'r'):
        return True

print(play())