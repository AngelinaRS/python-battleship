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
            return "First part h ship2"
        if guess_row == row_two_h1 and guess_column == column_two_h2:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part h ship2"

        if guess_row == row_two_v1 and guess_column == column_two_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "First part v ship2"

        if guess_row == row_two_v2 and guess_column == column_two_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part v2"
#-------------------------------------------------------------------------------

#-------------------THREE-----------------------------------------------------

    def put_ship_of_three_horizontal(self):
        row_three_h1 = self.random_row()
        column_three_h1 = self.random_column()

        column_three_h2 = column_three_h1+1
        column_three_h3 = column_three_h2+1

        if column_three_h1 == 10:
            column_three_h2 = column_three_h1-1
            column_three_h3 = column_three_h2-1

        return row_three_h1, column_three_h1, column_three_h2, column_three_h3

    def put_ship_of_three_vertical(self):
        row_three_v1 = self.random_row()
        column_three_v1 = self.random_column()

        row_three_v2 = row_three_v1+1
        row_three_v3 = row_three_v2+1

        if row_three_v1 == 10:
            row_three_v2 = row_three_v1-1
            row_three_v3 = row_three_v2-1

        return row_three_v1, column_three_v1, row_three_v2, row_three_v3

    def guess_ship_three(self, guess_row, guess_column, row_three_h1, column_three_h1, column_three_h2, column_three_h3,\
        row_three_v1, column_three_v1, row_three_v2, row_three_v3):

        if guess_row == row_three_h1 and guess_column == column_three_h1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "First part h ship3"

        if guess_row == row_three_h1 and guess_column == column_three_h2:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part h ship3"

        if guess_row == row_three_h1 and guess_column == column_three_h3:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Third part h ship3"

        if guess_row == row_three_v1 and guess_column == column_three_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "First par v ship3"

        if guess_row == row_three_v2 and guess_column == column_three_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part v ship3"

        if guess_row == row_three_v3 and guess_column == column_three_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Third part v ship3"
#--------------------------------------------------------------------------------

#-----------------------FOUR-----------------------------------------------------

    def put_ship_of_four_horizontal(self):
        row_four_h1 = self.random_row()
        column_four_h1 = self.random_column()

        column_four_h2 = column_four_h1+1
        column_four_h3 = column_four_h2+1
        column_four_h4 = column_four_h3+1

        if column_four_h1 == 10:
            column_four_h2 = column_four_h1-1
            column_four_h3 = column_four_h2-1
            column_four_h4 = column_four_h3-1

        return row_four_h1, column_four_h1, column_four_h2, column_four_h3, column_four_h4

    def put_ship_of_four_vertical(self):
        row_four_v1 = self.random_row()
        column_four_v1 = self.random_column()

        row_four_v2 = row_four_v1+1
        row_four_v3 = row_four_v2+1
        row_four_v4 = row_four_v3+1

        if row_four_v1 == 10:
            row_four_v2 = row_four_v1-1
            row_four_v3 = row_four_v2-1
            row_four_v4 = row_four_v3-1

        return row_four_v1, column_four_v1, row_four_v2, row_four_v3, row_four_v4

    def guess_ship_four(self, guess_row, guess_column, row_four_h1, column_four_h1, column_four_h2, column_four_h3, column_four_h4,\
        row_four_v1, column_four_v1, row_four_v2, row_four_v3, row_four_v4):

        if guess_row == row_four_h1 and guess_column == column_four_h1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Firs part h ship4"

        if guess_row == row_four_h1 and guess_column == column_four_h2:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part h ship4"

        if guess_row == row_four_h1 and guess_column == column_four_h3:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Third part h ship4"

        if guess_row == row_four_h1 and guess_column == column_four_h4:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Fourth part h ship4"

        if guess_row == row_four_v1 and guess_column == column_four_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "First part v ship4"

        if guess_row == row_four_v2 and guess_column == column_four_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Second part v ship4"

        if guess_row == row_four_v3 and guess_column == column_four_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Third part v ship4"

        if guess_row == row_four_v4 and guess_column == column_four_v1:
            self.board[guess_row-1][guess_column-1] = "*"
            self.reset()
            return "Fourth part v ship4"
#------------------------------------------------------------------------------------------------
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

    def message(self):
        print "You have shot to a part of the ship"

    def ask_to_the_user(self):
        self.generate_board()
        row_one_h, column_one_h = self.put_ship_of_one()

        row_two_h1, column_two_h1, column_two_h2 = self.put_ship_of_two_horizontal()
        row_two_v1, column_two_v1, row_two_v2 = self.put_ship_of_two_vertical()

        row_three_h1, column_three_h1, column_three_h2, column_three_h3 = self.put_ship_of_three_horizontal()
        row_three_v1, column_three_v1, row_three_v2, row_three_v3 = self.put_ship_of_three_vertical()

        row_four_h1, column_four_h1, column_four_h2, column_four_h3, column_four_h4 = self.put_ship_of_four_horizontal()
        row_four_v1, column_four_v1, row_four_v2, row_four_v3, row_four_v4 = self.put_ship_of_four_vertical()

        print "ship of one"
        print row_one_h, column_one_h
        print "\nship of two h"
        print row_two_h1, column_two_h1
        print row_two_h1, column_two_h2
        print "\nship of two v"
        print row_two_v1, column_two_v1
        print row_two_v2, column_two_v1
        print "\nship of three h"
        print row_three_h1, column_three_h1
        print row_three_h1, column_three_h2
        print row_three_h1, column_three_h3
        print "\nship of three v"
        print row_three_v1, column_three_v1
        print row_three_v2, column_three_v1
        print row_three_v3, column_three_v1
        print "\nship of four h"
        print row_four_h1, column_four_h1
        print row_four_h1, column_four_h2
        print row_four_h1, column_four_h3
        print row_four_h1, column_four_h4
        print "\nship of four v"
        print row_four_v1, column_four_v1
        print row_four_v2, column_four_v1
        print row_four_v3, column_four_v1
        print row_four_v4, column_four_v1

        while True:

            guess_row, guess_column = self.valid_row_and_column_given_by_user()

            ship_one = self.guess_ship_one(guess_row, guess_column, row_one_h, column_one_h)
            ship_two = self.guess_ship_two(guess_row, guess_column, row_two_h1, column_two_h1, column_two_h2, row_two_v1, column_two_v1, row_two_v2)
            ship_three = self.guess_ship_three(guess_row, guess_column, row_three_h1, column_three_h1, column_three_h2, column_three_h3, row_three_v1, column_three_v1, row_three_v2, row_three_v3)
            ship_four = self.guess_ship_four(guess_row, guess_column, row_four_h1, column_four_h1, column_four_h2, column_four_h3, column_four_h4, row_four_v1, column_four_v1, row_four_v2, row_four_v3, row_four_v4)

            if ship_one == True:
                print "You have sunk the ship of one piece"
                self.print_board()
            else:

                if ship_two == "First part h ship2" or ship_two == "Second part h ship2":
                    self.message()
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

if __name__ == '__main__':
    MAIN.menu()

