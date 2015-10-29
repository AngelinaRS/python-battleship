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

def random_row():
    return random.randint(1, 10)

def random_column():
    return random.randint(1, 10)

def ship_of_one():

    #board()
    row_one_h = random_row()
    column_one_h = random_column()
    return row_one_h, column_one_h

def put_ship_of_two_horizontal():

    row_two_h1 = random_row()
    column_two_h1 = random_column()

    column_two_h2 = column_two_h1+1

    if column_two_h1 == 10:
        column_two_h2 = column_two_h1-1

    return row_two_h1, column_two_h1, column_two_h2

#def ship_one(guess_row, guess_column, row_one_h, column_one_h):


def ask_to_the_user():
    board()
    row_one_h, column_one_h = ship_of_one()
    row_two_h1, column_two_h1, column_two_h2 = put_ship_of_two_horizontal()

    print "ship of one"
    print row_one_h
    print column_one_h

    print "ship of two"
    print row_two_h1
    print column_two_h1
    print ""
    print row_two_h1
    print column_two_h2

    while True:

        guess_row = input("\nGuess the row: ")
        guess_column = input("Guess the column: ")

        if guess_row == row_one_h and guess_column == column_one_h:
            BOARD[guess_row-1][guess_column-1] = "*"
            reset()
            print "You have sunk the ship of one piece"
            print_board()

        elif (guess_row == row_two_h1) and (guess_column == column_two_h1):
            BOARD[guess_row-1][guess_column-1] = "*"
            reset()
            print_board()
        elif (guess_row == row_two_h1) and (guess_column == column_two_h2):
            BOARD[guess_row-1][guess_column-1] = "*"
            reset()
            print_board()
        else:
            if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                reset()
                print "It is not in the ocean"
                print_board()

            elif (BOARD[guess_row-1][guess_column-1] == "X"):
                reset()
                print "Already You have written those coordinates"
                print_board()

            else:
                BOARD[guess_row-1][guess_column-1] = "X"
                reset()
                print "Try again "
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



