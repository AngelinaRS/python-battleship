"Battleship"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import sys

BOARD = []

def reset():
    """This cleans the screen"""
    if os.name == "posix": #In linux
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"): #In windows
        os.system("cls")
reset()

def press_enter():
    """This saves the intruction -PRESS ENTER-"""

    press = raw_input("\n\nPRESS --ENTER--   ")
    reset()
    menu()

def board():

    for lista in range(0, 10):
        BOARD.append(["O"] * 10)

def print_board():

    for o in BOARD:
        print " ".join(o)

def random_file():
    return random.randint(1, 10)

def random_column():
    return random.randint(1, 10)

def ship_of_one():

    board()
    file_board = random_file()
    column_board = random_column()
    return file_board, column_board

def ask_to_the_user():
    file_board, column_board = ship_of_one()
    print file_board
    print column_board

    while True:

        guess_file = input("\nGuess the file: ")
        guess_column = input("Guess the column: ")

        if guess_file == file_board and guess_column == column_board:
            BOARD[guess_file-1][guess_column-1] = "*"
            reset()
            print "Guessed"
            print_board()
            press_enter()
        else:
            BOARD[guess_file-1][guess_column-1] = "X"
            reset()
            print "No"
            print_board()

def menu_print():
    """This saves the instructions of the game"""

    print "Welcome to Battleship"
    print "\nChoose an option that you want"
    print "\n 1. Single Player"
    print "\n 2. Two Players"
    print "\n 3. Exit"

def menu_option():
    """This saves the election of the user"""

    while True:

        choose_user = raw_input(" - ")

        if choose_user == "1":
            reset()
            ask_to_the_user()

        elif choose_user == "2":
            pass

        elif choose_user == "3":
            reset()
            sys.exit()

        else:
            reset()
            print "*Choose a valid option\n"
            menu()

def menu():
    """This saves the menu"""

    menu_print()
    menu_option()

menu()



