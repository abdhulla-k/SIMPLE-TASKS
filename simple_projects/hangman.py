import random
from words import words
import string

def get_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_word(words)
    word_letter = set(word.upper()) # created a set that containing the letters of the selected word by computer
    print('word letter')
    print(word_letter)
    #alphabet = set(string.ascii_uppercase)
    #rint('it is alphabet')
    #print(alphabet)
    used_letters = set() # what the user has guessede

    while len(word_letter) > 0:
        # user input
        print('you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        global letter 
        
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in word_letter:
            letter = user_letter
            used_letters.add(user_letter)
            if user_letter in word_letter:
             word_letter.remove(user_letter)
        
        elif user_letter in used_letters:
            print('you have already used that charactor. please try again.')
        
        else:
            print('Invalid charactor. please try again.')
        
            

hangman()
user_input = input('Type something:')
print(user_input)
    