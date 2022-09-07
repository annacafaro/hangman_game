"""THE HANGMAN GAME
Guess the letters to a secret word before the hangman is drawn.

Author: Anna Cafaro
Python Version: 3.9.4
This code is available at 

Features for new realeses: 
- update_screen() with any OS
"""



import platform
from numpy.random import randint
from os import system
import menu_and_ascii_sprites as SPRITES


FILE_PATH = './files/data.txt'


def update_screen():
    
    system('cls')


def red_data(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.stip().upper())
    return words


def main():
    PLATFORM = platform.system()
    #data = read_data(FILE_PATH)
    #print(SPRITES.menu)


if __name__ == '__main__':
    main()
