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
        self.board_to_check = []

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

    def generate_board_to_check(self):
        for lis in range(0, 10):
            self.board_to_check.append(["O"] * 10)

    def generate_board(self):

        for lista in range(0, 10):
            self.board.append(["O"] * 10)

    def print_board(self):
        print "Starts the battle ship"
        print "Remember when you guess right the position of one part of the ship"
        print "will appear this symbol -*-"
        print "when you do not guess right, will appear this symbol -X-\n\n"
        for o in self.board:
            print " ".join(o)

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

    def valid_position_bomb(self):
        #self.generate_board_to_check()

        row_bomb = random.randint(1, 10)
        column_bomb = random.randint(1, 10)

        bomb = True
        while bomb == True:
            if self.board_to_check[row_bomb-1][column_bomb-1] == "O":
                self.board_to_check[row_bomb-1][column_bomb-1] == "*"
                return row_bomb, column_bomb
                break

            elif self.board_to_check[row_bomb-1][column_bomb-1] == "*":
                row_bomb = random.randint(1, 10)
                column_bomb = random.randint(1, 10)
                bomb = True
        #return row_bomb, column_bomb

    def valid_position_ship_two_horizontal(self):
        #self.generate_board_to_check()

        row_ship_two_horizontal = random.randint(1,9)
        column_ship_two_horizontal = random.randint(1,9)

        ship2 = True
        while ship2 == True:

            if self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "O" and self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "O":
                self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                return row_ship_two_horizontal, column_ship_two_horizontal
                break

            elif self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                row_ship_two_horizontal = random.randint(1,9)
                column_ship_two_horizontal = random.randint(1,9)
                ship2 = True

    def valid_position_ship_two_vertical(self):
        row_ship_two_vertical = random.randint(1,9)
        column_ship_two_vertical = random.randint(1,9)


        ship2 = True
        while ship2 == True:
            if self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "O" and self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical] == "O":
                self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical] = "*"
                return row_ship_two_vertical, column_ship_two_vertical
                break

            elif self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical] == "*":
                row_ship_two_vertical = random.randint(1,9)
                column_ship_two_vertical = random.randint(1,9)
                ship2 = True
        return row_ship_two_vertical, column_ship_two_vertical

    def valid_position_ship_three_horizontal(self):

        row_ship_three_horizontal = random.randint(1,8)
        column_ship_three_horizontal = random.randint(1,8)

        ship3 = True
        while ship3 == True:
            if self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "O" and self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "O"\
            and self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "O":

                self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                return row_ship_three_horizontal, column_ship_three_horizontal
                break

            elif self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
            or self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                row_ship_three_horizontal = random.randint(1,8)
                column_ship_three_horizontal = random.randint(1,8)
                ship3 = True

    def valid_position_ship_three_vertical(self):

        row_ship_three_vertical = random.randint(1,8)
        column_ship_three_vertical = random.randint(1,8)

        ship3 = True
        while ship3 == True:
            if self.board_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "O" and self.board_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "O"\
            and self.board_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "O":
                self.board_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                self.board_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                self.board_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                return row_ship_three_vertical, column_ship_three_vertical
                break

            elif self.board_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
            or self.board_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                row_ship_three_vertical = random.randint(1,8)
                column_ship_three_vertical = random.randint(1,8)
                ship3 = True

    def valid_position_ship_four_horizontal(self):
        row_ship_four_horizontal = random.randint(1,7)
        column_ship_four_horizontal = random.randint(1,7)

        ship4 = True
        while ship4 == True:
            if self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "O" and self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "O"\
            and self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "O" and self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "O":

                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*"
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*"
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*" 
                return row_ship_four_horizontal, column_ship_four_horizontal
                break

            elif self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
            or self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":

                row_ship_four_horizontal = random.randint(1,7)
                column_ship_four_horizontal = random.randint(1,7)
                ship4 = True

    def valid_position_ship_four_vertical(self):

        row_ship_four_vertical = random.randint(1,7)
        column_ship_four_vertical = random.randint(1,7)

        ship4 = True
        while ship4 == True:
            if self.board_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "O" and self.board_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "O"\
            and self.board_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "O" and self.board_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "O":

                self.board_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*"
                self.board_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"
                self.board_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*"
                self.board_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*"

                return row_ship_four_vertical, column_ship_four_vertical
                break

            elif self.board_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
            or self.board_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":

                row_ship_four_vertical = random.randint(1,7)
                column_ship_four_vertical = random.randint(1,7)
                ship4 = True

    def guess_ship_user(self, guess_row, guess_column, row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal, row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal,\
        column_ship_three_horizontal, row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical):

        if guess_row == row_bomb and guess_column == column_bomb:
            self.board[guess_row-1][guess_column-1] == "#"
            self.reset()
            return True
#-------------------------Ship two horizontal------------------------------------------------------

        if guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal:
            self.board[guess_row-1][guess_column-1] == "*"
            self.reset()
            return "First part h ship2"

        if guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal+1:
            self.board[guess_row-1][guess_column] == "*"
            self.reset()
            return "Second part h ship2"

#-----------------------Ship two vertical------------------------------------------------------------

        if guess_row == row_ship_two_vertical and guess_column == column_ship_two_vertical:
            self.board[guess_row-1][guess_column] == "*"
            self.reset()
            return "First part v ship2"

        if guess_row == row_ship_two_vertical+1 and guess_column == column_ship_two_vertical:
            self.board[guess_row][guess_column] == "*"
            self.reset()
            return "Second part v ship2"

#-----------------------Ship three horizontal-----------------------------------------------------------

        if guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal:
            self.board[guess_row-1][guess_column-1] == "*"
            self.reset()
            return "First part h ship3"

        if guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+1:
            self.board[guess_row-1][guess_column] == "*"
            self.reset()
            return "Second part h ship3"

        if guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+2:
            self.board[guess_row-1][guess_column+1] == "*"
            self.reset()
            return "Third part h ship3"

#-----------------------Ship three vertical----------------------------------------------------------------

        if guess_row == row_ship_three_vertical and guess_column == column_ship_three_vertical:
            self.board[guess_row-1][guess_column-1] == "*"
            self.reset()
            return "First part v ship3"

        if guess_row == row_ship_three_vertical+1 and guess_column == column_ship_three_vertical:
            self.board[guess_row][guess_column-1] == "*"
            self.reset()
            return "Second part v ship3"

        if guess_row == row_ship_three_vertical+2 and guess_column == column_ship_three_vertical:
            self.board[guess_row+1][guess_column-1] == "*"
            self.reset()
            return "Third part v ship3"

#-----------------------Ship four horizontal----------------------------------------------------------------

        if guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal:
            self.board[guess_row-1][guess_column-1] == "*"
            self.reset()
            return "First part h ship4"

        if guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+1:
            self.board[guess_row-1][guess_column] == "*"
            self.reset()
            return "Second part h ship4"

        if guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+2:
            self.board[guess_row-1][guess_column+1] == "*"
            self.reset()
            return "Third part h ship4"

        if guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+3:
            self.board[guess_row-1][guess_column+2] == "*"
            self.reset()
            return "Fourth part h ship4"

#-----------------------Ship four vertical--------------------------------------------------------------------

        if guess_row == row_ship_four_vertical and guess_column == column_ship_four_vertical:
            self.board[guess_row-1][guess_column-1] == "*"
            self.reset()
            return "First part v ship4"

        if guess_row == row_ship_four_vertical+1 and guess_column == column_ship_four_vertical:
            self.board[guess_row][guess_column-1] == "*"
            self.reset()
            return "Second part v ship4"

        if guess_row == row_ship_four_vertical+2 and guess_column == column_ship_four_vertical:
            self.board[guess_row+1][guess_column-1] == "*"
            self.reset()
            return "Third part v ship4"

        if guess_row == row_ship_four_vertical+3 and guess_column == column_ship_four_vertical:
            self.board[guess_row+2][guess_column-1] == "*"
            self.reset()
            return "Fourth part v ship4"


    def ask_to_the_user(self):
        self.generate_board_to_check()
        self.generate_board()

        #row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal, row_ship_two_vertical, column_ship_two_vertical,\
        #row_ship_three_horizontal, column_ship_three_horizontal, row_ship_three_vertical, column_ship_three_vertical,\
        #row_ship_four_horizontal, column_ship_four_horizontal,row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship()

        row_bomb, column_bomb = self.valid_position_bomb()
        row_ship_two_horizontal, column_ship_two_horizontal = self.valid_position_ship_two_horizontal()
        row_ship_two_vertical, column_ship_two_vertical = self.valid_position_ship_two_vertical()
        row_ship_three_horizontal, column_ship_three_horizontal = self. valid_position_ship_three_horizontal()
        row_ship_three_vertical, column_ship_three_vertical = self.valid_position_ship_three_vertical()
        row_ship_four_horizontal, column_ship_four_horizontal = self.valid_position_ship_four_horizontal()
        row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship_four_vertical()


        print "bomb"
        print row_bomb, column_bomb
        print "\nship of two h"
        print row_ship_two_horizontal, column_ship_two_horizontal
        print "\nship of two v"
        print row_ship_two_vertical, column_ship_two_vertical

        print "\nship of three h"
        print row_ship_three_horizontal, column_ship_three_horizontal

        print "\nship of three v"
        print row_ship_three_vertical, column_ship_three_vertical

        print "\nship of four h"
        print row_ship_four_horizontal, column_ship_four_horizontal

        print "\nship of four v"
        print row_ship_four_vertical, column_ship_four_vertical

        while True:

            guess_row, guess_column = self.valid_row_and_column_given_by_user()

            guess_ship = self.guess_ship_user(guess_row, guess_column, row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal, row_ship_two_vertical, column_ship_two_vertical,\
                row_ship_three_horizontal, column_ship_three_horizontal, row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
                row_ship_four_vertical, column_ship_four_vertical)

            if guess_ship == True:
                self.print_board()
                print "You have shot to the bomb, and You have sunk all the ships"
                print "You win"
                self.press_enter()
            if guess_ship == "First part h ship2" or guess_ship == "Second part h ship2"\
                or guess_ship == "First part v ship2" or guess_ship == "Second part v ship2"\
                or guess_ship == "First part h ship3" or guess_ship == "Second part h ship3" or guess_ship == "Third part h ship3"\
                or guess_ship == "First part v ship3" or guess_ship == "Second part v ship3" or guess_ship == "Third part v ship3"\
                or guess_ship == "First part h ship4" or guess_ship == "Second part h ship4" or guess_ship == "Third part h ship4" or guess_ship == "Fourth part h ship4"\
                or guess_ship == "First part v ship4" or guess_ship == "Second part v ship4" or guess_ship == "Third part v ship4" or guess_ship == "Fourth part v ship4":
                    #self.message()
                    self.print_board()
            else:

                if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                    self.reset()
                    print "It is not in the ocean\n\n"
                    self.print_board()

                elif self.board[guess_row-1][guess_column-1] == "X":
                    self.reset()
                    print "Already You have written those coordinates\n\n"
                    self.print_board()
                else:
                    self.board[guess_row-1][guess_column-1] = "X"
                    self.reset()
                    print "Try again\n\n"
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

