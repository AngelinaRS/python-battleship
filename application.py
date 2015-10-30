"Battleship"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import sys

class SinglePlayer(object):
    """This class saves the game for one player"""
    def __init__(self):

        self.board = []

    def reset(self):
        """This cleans the screen"""
        if os.name == "posix": #In linux
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"): #In windows
            os.system("cls")

    def press_enter(self):
        """This saves the intruction -PRESS ENTER-"""

        press = raw_input("\n\nPRESS --ENTER--   ")
        self.reset()
        self.menu()

    def generate_board(self):

        for lista in range(0, 10):
            self.board.append(["O"] * 10)

    def print_board(self):

        for o in self.board:
            print " ".join(o)

    def random_row(self):
        return random.randint(1, 10)

    def random_column(self):
        return random.randint(1, 10)

#--------------ONE---------------------------------------

    def put_ship_of_one(self):

        row_one_h = self.random_row()
        column_one_h = self.random_column()
        return row_one_h, column_one_h

    def guess_ship_one(self, guess_row, guess_column, row_one_h, column_one_h):
        if guess_row == row_one_h and guess_column == column_one_h:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return True
#-------------------------------------------------------------------------

#------------TWO--------------------------------------------------
    def put_ship_of_two_horizontal(self):

        row_two_h1 = self.random_row()
        column_two_h1 = self.random_column()

        column_two_h2 = column_two_h1+1

        if column_two_h1 == 10:
            column_two_h2 = column_two_h1-1

        return row_two_h1, column_two_h1, column_two_h2

    def put_ship_of_two_vertical(self):
        row_two_v1 = self.random_row()
        column_two_v1 = self.random_column()

        row_two_v2 = row_two_v1+1

        if row_two_v1 == 10:
            row_two_v2 = row_two_v1-1

        return row_two_v1, column_two_v1, row_two_v2

    def guess_ship_two(self, guess_row, guess_column, row_two_h1, column_two_h1, column_two_h2, row_two_v1, column_two_v1, row_two_v2):

        if guess_row == row_two_h1 and guess_column == column_two_h1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "First part h"
        if guess_row == row_two_h1 and guess_column == column_two_h2:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part h"
#-------------------------------------------------------------------------------



    def valid_row_and_column_given_by_user(self):

        while True:
            try:
                guess_row = raw_input("\nGuess the row: ")
                guess_row = int(guess_row)
                guess_column = raw_input("Guess the column: ")
                guess_column = int(guess_column)
                return guess_row, guess_column
            except ValueError:
                self.reset()
                print "Only can insert integer numbers"
        return guess_row, guess_column

    def ask_to_the_user(self):
        self.generate_board()
        row_one_h, column_one_h = self.put_ship_of_one()
        row_two_h1, column_two_h1, column_two_h2 = self.put_ship_of_two_horizontal()
        row_two_v1, column_two_v1, row_two_v2 = self.put_ship_of_two_vertical()

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

            guess_row, guess_column = self.valid_row_and_column_given_by_user()

            ship_one = self.guess_ship_one(guess_row, guess_column, row_one_h, column_one_h)
            ship_two = self.guess_ship_two(guess_row, guess_column, row_two_h1, column_two_h1, column_two_h2, row_two_v1, column_two_v1, row_two_v2)

            if ship_one == True:
                print "You have sunk the ship of one piece"
                self.print_board()
            else:

                if ship_two == "First part h" or ship_two == "Second part h":
                    print "You have shot to a part of the ship"
                    self.print_board()
                else:

                    if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                        self.reset()
                        print "It is not in the ocean"
                        self.print_board()

                    elif (self.board[guess_row-1][guess_column-1] == "X"):
                        self.reset()
                        print "Already You have written those coordinates"
                        self.print_board()

                    else:
                        self.board[guess_row-1][guess_column-1] = "X"
                        self.reset()
                        print "Try again "
                        self.print_board()

    def menu_print(self):
        """This saves the instructions of the game"""

        print "Welcome to Battleship"
        print "\nChoose an option that you want"
        print "\n 1. Single Player"
        print "\n 2. Two Players"
        print "\n 3. Exit"

    def menu_option(self):
        """This saves the election of the user"""

        while True:

            choose_user = raw_input(" - ")

            if choose_user == "1":
                self.reset()
                self.ask_to_the_user()

            elif choose_user == "2":
                pass

            elif choose_user == "3":
                self.reset()
                sys.exit()

            else:
                self.reset()
                print "*Choose a valid option\n"
                self.menu()

    def menu(self):
        """This saves the menu"""

        self.menu_print()
        self.menu_option()

MAIN = SinglePlayer()

MAIN.menu()

