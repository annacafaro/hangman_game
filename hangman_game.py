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
    """Cleans the console screen depending on the type 
    of the Operating System you are on.

    Args:
        active_os (str): the Operating System of the coumputer
    """
    if active_os == 'Windows':
        system('cls')
    elif active_os == 'Linux' or active_os == 'Darwin':
        system('clear')


def read_data(file_path):
    """Reading the file of possible words to guess and assigning
    them to a list. 

    Args:
        file_path (str): path where the file of data is stored

    Returns:
        list: the list of possible words to guess
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip().lower() for line in f]
    return words


def get_player_guess(already_entered):
    """Returns the letter the player entered. Also, this function 
    checks whether the input is a valid character and a different
    letter from the previous inputs.

    Args:
        already_entered (list): concatenated list of the missed 
                                and correctly-guessed letters

    Returns:
        str: the letter entered by the user
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


def draw_hangman(missed_letters, right_guessed, secret_word):
    """Draw the current state of the hangman, along with the
    missed and correctly-guessed letters of the secret word.

    Args:
        missed_letters (list): the missed letters
        right_guessed (list): the correctly-guessed letters
        secret_word (str): the secret word that the player needs to guess
    """
    print(SPRITES.HANGMAN_PICS[len(missed_letters)] + '\n\n')

    # Display the blanks for the secret word (one blank per letter)
    blanks = ['_'] * len(secret_word)

    # Replace blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in right_guessed:
            blanks[i] = secret_word[i]

    # Show the incorrectly guessed letters
    if len(missed_letters) == 0:
        print('\n\nGREAT JOB! No missed letters yet.')
    print('\n\nOPS! Your missed letters are: ')
    for letter in missed_letters:
        print(letter + ', ')
    print('\n\n')


def main():

    # Detecting the Operating System for the clear_screen function. 
    ACTIVE_OS = platform.system()

    # Set up for the variables of the game:
    missed_letters = []
    right_guessed = []
    data = read_data(FILE_PATH)
    random_word = data[randint(0, len(data))]
    # The word the player must guess. After removing characters with accent marks.
    secret_word = random_word.translate(random_word.maketrans('áéíóú', 'aeiou'))  

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

