"""THE HANGMAN GAME
Guess the letters to a secret word before the hangman is drawn.

Author: Anna Cafaro
Python Version: 3.9.4
This code is available at 

Features for new realeses: 
- add sprites for winner and loser
- ask the language of the words and create a file with english words
"""



import platform
import sys
from random import randint
from os import system
import menu_and_ascii_sprites as SPRITES


FILE_PATH = './files/data.txt'


def update_screen(active_os):
    if active_os == 'Windows':
        system('cls')
    elif active_os == 'Linux' or active_os == 'Darwin':
        system('clear')


def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip().lower() for line in f]
    return words


def main():

    ACTIVE_OS = platform.system()
    missed_letters = []
    right_guessed = []

    data = read_data(FILE_PATH)
    secret_word = data[randint(0, len(data))]

    game_status = int(input(SPRITES.MENU))

    if game_status == 1: 
        pass
    else:
        print(SPRITES.EXIT)
        sys.exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If 'Ctrl+C' is pressed, end the program. 
        sys.exit()

