"""THE HANGMAN GAME
Guess the letters to a secret word before the hangman is drawn.

Author: Anna Cafaro
Python Version: 3.9.4
This code is available at 

Features for new realeses: 
- improve the while-loop of get_player_guess
- add sprites for winner and loser
- ask the language of the words and create a file with english words
- increase the difficulty of the words and add a clue system
"""



import platform
import sys
from random import randint
from os import system
import menu_and_ascii_sprites as SPRITES


FILE_PATH = './files/data.txt'


def clear_screen(active_os):
    if active_os == 'Windows':
        system('cls')
    elif active_os == 'Linux' or active_os == 'Darwin':
        system('clear')


def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip().lower() for line in f]
    return words


def get_player_guess(already_entered):
    """Returns the letter the player entered. Also, this function 
    checks whether the input is a valid character and a different
    letter from the previous inputs.
    """
    while True:  # Keep asking until the player enters a valid letter.
        print('Guess a letter.')
        guess = input('-> ').lower()
        if len(guess) != 1:
            raise ValueError('Please enter a single letter.')
        elif guess in already_entered:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            raise ValueError('Please enter a letter. Numbers and other characters are not valid')
        else:
            return guess



def main():

    # Detecting the Operative System for the clear_screen function. 
    ACTIVE_OS = platform.system()

    # Set up for the variables of the game:
    missed_letters = []  # List of incorrect letter guesses.
    right_guessed = []  # List of correct letter guesses.
    data = read_data(FILE_PATH)
    secret_word = data[randint(0, len(data))] # The word the player must guess. 

    game_status = int(input(SPRITES.MENU))

    if game_status == 1: 
        guess = get_player_guess(missed_letters + right_guessed)
        print(guess)
    else:
        print(SPRITES.EXIT)
        sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If 'Ctrl+C' is pressed, end the program. 
        sys.exit()

