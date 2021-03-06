"Battleship"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import sys
import time

class GameBattle(object):
    """This class saves the elaboration of the ships"""
    def __init__(self):

        self.board_player_one = []
        self.board_player_one_to_check = []

        self.board_player_two = []
        self.board_player_two_to_check = []

        self.show_board_one = []
        self.show_board_two = []

    def reset(self):
        """This cleans the screen"""
        if os.name == "posix": #In linux
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"): #In windows
            os.system("cls")

    def clean_lists(self):
        del self.board_player_one[:]
        del self.board_player_one_to_check[:]
        del self.board_player_two[:]
        del self.board_player_two_to_check[:]
        del self.show_board_one[:]
        del self.show_board_two[:]

#***************BOARD PLAYER ONE TO CHECK*********************
    def generate_board_player_one_to_check(self):
        for l in range(0, 10):
            self.board_player_one_to_check.append(["-"] * 10)

    def print_board_player_one_to_check(self):

        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|"

#*************BOARD PLAYER ONE*********************************
    def generate_board_player_one(self):

        for l in range(0, 10):
            self.board_player_one.append(["-"] * 10)

    def print_board_player_one(self):
        #self.reset()
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.board_player_one:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

#**************BOARD PLAYER TWO TO CHECK*****************************
    def generate_board_player_two_to_check(self):

        for l in range(0, 10):
            self.board_player_two_to_check.append(["-"] * 10)

    def print_board_player_two_to_check(self):

        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

#**************BOARD PLAYER TWO*******************************************
    def generate_board_player_two(self):

        for l in range(0, 10):
            self.board_player_two.append(["-"] * 10)

    def print_board_player_two(self):

        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.board_player_two:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

#***************BOARDS TO HELP TO PUT THE SHIPS********************************

    def generate_show_board_one(self):

        for l in range(0, 10):
            self.show_board_one.append(["-"]*10)

    def print_show_board_one(self):
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.show_board_one:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

    def generate_show_board_two(self):

        for l in range(0, 10):
            self.show_board_two.append(["-"]*10)

    def print_show_board_two(self):
        #self.reset()
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.show_board_two:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

#************************************************************************************

    def print_players(self, player):

        if player == "1":
            print """
    ____  __    _____  ____________     ___
   / __ \/ /   /   \ \/ / ____/ __ \   <  /
  / /_/ / /   / /| |\  / __/ / /_/ /   / / 
 / ____/ /___/ ___ |/ / /___/ _, _/   / /  
/_/   /_____/_/  |_/_/_____/_/ |_|   /_/  \n"""

        elif player == "2":
            print """
    ____  __    _____  ____________     ___  
   / __ \/ /   /   \ \/ / ____/ __ \   |__ \ 
  / /_/ / /   / /| |\  / __/ / /_/ /   __/ / 
 / ____/ /___/ ___ |/ / /___/ _, _/   / __/  
/_/   /_____/_/  |_/_/_____/_/ |_|   /____/  
                                            \n"""

        elif player == "1w":
            print """
    ____  __    _____  ____________     ___     _       _______   __
   / __ \/ /   /   \ \/ / ____/ __ \   <  /    | |     / /  _/ | / /
  / /_/ / /   / /| |\  / __/ / /_/ /   / /     | | /| / // //  |/ / 
 / ____/ /___/ ___ |/ / /___/ _, _/   / /      | |/ |/ // // /|  /  
/_/   /_____/_/  |_/_/_____/_/ |_|   /_/       |__/|__/___/_/ |_/   
"""

        elif player == "2w":
            print """
    ____  __    _____  ____________     ___        _       _______   __
   / __ \/ /   /   \ \/ / ____/ __ \   |__ \      | |     / /  _/ | / /
  / /_/ / /   / /| |\  / __/ / /_/ /   __/ /      | | /| / // //  |/ / 
 / ____/ /___/ ___ |/ / /___/ _, _/   / __/       | |/ |/ // // /|  /  
/_/   /_____/_/  |_/_/_____/_/ |_|   /____/       |__/|__/___/_/ |_/   
                                                                       """

        elif player == "b1":
            print "\n   BOARD PLAYER  1"
        elif player == "b2":
            print "\n   BOARD PLAYER  2"


    def show_board_one_or_two(self, board):
        if board == "1":
            self.reset()
            time.sleep(1)
            self.print_players("b1")
            self.print_show_board_one()

        elif board == "2":
            self.reset()
            time.sleep(1)
            self.print_players("b2")
            self.print_show_board_two()

    def valid_insert_row_and_column_by_user(self):

        while True:
            try:
                insert_row = raw_input("\nInsert row: ")
                insert_row = int(insert_row)
                insert_column = raw_input("Insert column: ")
                insert_column = int(insert_column)
                return insert_row, insert_column
            except ValueError:
                self.reset()
                print "Only can insert integer numbers"
        return insert_row, insert_column


#**************VALID POSITIONS**********************************************

    def valid_position_bomb(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            bomb = True
            while bomb == True:
                row_bomb = random.randint(1, 10)
                column_bomb = random.randint(1, 10)
                if self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "-":
                    self.board_player_one_to_check[row_bomb-1][column_bomb-1] = "*"
                    return row_bomb, column_bomb
                    break

                elif self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "*":
                    bomb = True

        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the bomb"
            bomb = True
            while bomb == True:
                row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                if row_bomb > 10 or row_bomb < 1 or column_bomb > 10 or row_bomb <1:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    bomb = True
                else:
                    if self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "-":
                        self.board_player_one_to_check[row_bomb-1][column_bomb-1] = "*"
                        return row_bomb, column_bomb
                        break

                    elif self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        bomb = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the bomb"
            bomb = True
            while bomb == True:
                row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                if row_bomb > 10 or row_bomb < 1 or column_bomb > 10 or row_bomb <1:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    bomb = True
                else:
                    if self.board_player_two_to_check[row_bomb-1][column_bomb-1] == "-":
                        self.board_player_two_to_check[row_bomb-1][column_bomb-1] = "*"
                        return row_bomb, column_bomb
                        break

                    elif self.board_player_two_to_check[row_bomb-1][column_bomb-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                        bomb = True

    def valid_position_ship_two_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            ship2 = True
            while ship2 == True:
                row_ship_two_horizontal = random.randint(1,10)
                column_ship_two_horizontal = random.randint(1,9)

                if self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                    return row_ship_two_horizontal, column_ship_two_horizontal
                    break

                elif self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                    ship2 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the ship"
            print "of two parts in horizontal orientation\n"

            ship2 = True
            while ship2 == True:
                row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_two_horizontal < 1 or row_ship_two_horizontal > 10 or column_ship_two_horizontal < 1 or column_ship_two_horizontal > 9:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship2 = True
                else:
                    if self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                        self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                        self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                        return row_ship_two_horizontal, column_ship_two_horizontal
                        break

                    elif self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        ship2 = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the ship"
            print "of two parts in horizontal orientation\n"

            ship2 = True
            while ship2 == True:
                row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_two_horizontal < 1 or row_ship_two_horizontal > 10 or column_ship_two_horizontal < 1 or column_ship_two_horizontal > 9:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship2 = True
                else:
                    if self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                        self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                        self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                        return row_ship_two_horizontal, column_ship_two_horizontal
                        break

                    elif self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        ship2 = True

    def valid_position_ship_two_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            ship2 = True
            while ship2 == True:
                row_ship_two_vertical = random.randint(1,9)
                column_ship_two_vertical = random.randint(1,10)
                if self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                    return row_ship_two_vertical, column_ship_two_vertical
                    break

                elif self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                    ship2 = True

        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the ship"
            print "of two parts in vertical orientation\n"

            ship2 = True
            while ship2 == True:
                row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_two_vertical < 1 or row_ship_two_vertical > 9 or column_ship_two_vertical < 1 or column_ship_two_vertical > 10:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship2 = True
                else:
                    if self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "-":
                        self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                        return row_ship_two_vertical, column_ship_two_vertical
                        break

                    elif self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        ship2 = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the ship"
            print "of two parts in vertical orientation\n"

            ship2 = True
            while ship2 == True:
                row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_two_vertical < 1 or row_ship_two_vertical > 9 or column_ship_two_vertical < 1 or column_ship_two_vertical > 10:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship2 = True
                else:
                    if self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_two_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "-":
                        self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                        return row_ship_two_vertical, column_ship_two_vertical
                        break

                    elif self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        ship2 = True

    def valid_position_ship_three_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            ship3 = True
            while ship3 == True:
                row_ship_three_horizontal = random.randint(1,10)
                column_ship_three_horizontal = random.randint(1,8)
                if self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":

                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                    return row_ship_three_horizontal, column_ship_three_horizontal
                    break

                elif self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                    ship3 = True

        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the ship"
            print "of three parts in horizontal orientation\n"

            ship3 = True
            while ship3 == True:
                row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_three_horizontal < 1 or row_ship_three_horizontal > 10 or column_ship_three_horizontal < 1 or column_ship_three_horizontal > 8:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship3 = True
                else:

                    if self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                    and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":

                        self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                        self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                        self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                        return row_ship_three_horizontal, column_ship_three_horizontal
                        break
                    elif self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                    or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        ship3 = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the ship"
            print "of three parts in horizontal orientation\n"

            ship3 = True
            while ship3 == True:
                row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_three_horizontal < 1 or row_ship_three_horizontal > 10 or column_ship_three_horizontal < 1 or column_ship_three_horizontal > 8:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship3 = True
                else:
                    if self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                    and self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":

                        self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                        self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                        self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                        return row_ship_three_horizontal, column_ship_three_horizontal
                        break
                    elif self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                    or self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        ship3 = True

    def valid_position_ship_three_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            ship3 = True
            while ship3 == True:
                row_ship_three_vertical = random.randint(1,8)
                column_ship_three_vertical = random.randint(1,10)
                if self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                    return row_ship_three_vertical, column_ship_three_vertical
                    break

                elif self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                    ship3 = True

        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the ship"
            print "of three parts in vertical orientation\n"

            ship3 = True
            while ship3 == True:
                row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_three_vertical < 1 or row_ship_three_vertical > 8 or column_ship_three_vertical < 1 or column_ship_three_vertical > 10:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship3 = True
                else:
                    if self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                    and self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                        self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                        return row_ship_three_vertical, column_ship_three_vertical
                        break

                    elif self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                    or self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        ship3 = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the ship"
            print "of three parts in vertical orientation\n"

            ship3 = True
            while ship3 == True:
                row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_three_vertical < 1 or row_ship_three_vertical > 8 or column_ship_three_vertical < 1 or column_ship_three_vertical > 10:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship3 = True
                else:
                    if self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                    and self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                        self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                        return row_ship_three_vertical, column_ship_three_vertical
                        break

                    elif self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                    or self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        ship3 = True

    def valid_position_ship_four_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            ship4 = True
            while ship4 == True:
                row_ship_four_horizontal = random.randint(1,10)
                column_ship_four_horizontal = random.randint(1,7)
                if self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "-":

                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                    return row_ship_four_horizontal, column_ship_four_horizontal
                    break

                elif self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                    ship4 = True

        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the ship"
            print "of four parts in horizontal orientation\n"

            ship4 = True
            while ship4 == True:
                row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_four_horizontal < 1 or row_ship_four_horizontal > 10 or  column_ship_four_horizontal < 1 or column_ship_four_horizontal > 7:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship4 = True
                else:
                    if self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "-"\
                    and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "-":

                        self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                        self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                        self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                        self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                        return row_ship_four_horizontal, column_ship_four_horizontal
                        break

                    elif self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
                    or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        ship4 = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the ship"
            print "of four parts in horizontal orientation\n"

            ship4 = True
            while ship4 == True:
                row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_four_horizontal < 1 or row_ship_four_horizontal > 10 or  column_ship_four_horizontal < 1 or column_ship_four_horizontal > 7:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship4 = True
                else:
                    if self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "-"\
                    and self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "-" and self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "-":

                        self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                        self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                        self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                        self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                        return row_ship_four_horizontal, column_ship_four_horizontal
                        break

                    elif self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
                    or self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        ship4 = True

    def valid_position_ship_four_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()

        if aleatory_or_no == "aleatory":

            ship4 = True
            while ship4 == True:
                row_ship_four_vertical = random.randint(1,7)
                column_ship_four_vertical = random.randint(1,10)
                if self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "-":

                    self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"

                    return row_ship_four_vertical, column_ship_four_vertical
                    break

                elif self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                    ship4 = True

        elif aleatory_or_no == "no aleatory one":
            print "\nInsert your coordinates to put the ship"
            print "of four parts in vertical orientation\n"

            ship4 = True
            while ship4 == True:
                row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_four_vertical < 1 or row_ship_four_vertical > 7 or column_ship_four_vertical < 1 or column_ship_four_vertical > 10:
                    self.show_board_one_or_two("1")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship4 = True
                else:
                    if self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "-"\
                    and self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "-":

                        self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"
                        return row_ship_four_vertical, column_ship_four_vertical
                        break

                    elif self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
                    or self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nThere is a ship in this coordinate\n"
                        ship4 = True

        elif aleatory_or_no == "no aleatory two":
            print "\nInsert your coordinates to put the ship"
            print "of four parts in vertical orientation\n"

            ship4 = True
            while ship4 == True:
                row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_four_vertical < 1 or row_ship_four_vertical > 7 or column_ship_four_vertical < 1 or column_ship_four_vertical > 10:
                    self.show_board_one_or_two("2")
                    print "\nThis ship leaves of the ocean, insert other coordinates"
                    ship4 = True
                else:
                    if self.board_player_two_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "-" and self.board_player_two_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "-"\
                    and self.board_player_two_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "-" and self.board_player_two_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "-":

                        self.board_player_two_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"
                        return row_ship_four_vertical, column_ship_four_vertical
                        break

                    elif self.board_player_two_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_player_two_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
                    or self.board_player_two_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_player_two_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nThere is a ship in this coordinate\n"
                        ship4 = True

class SinglePlayer(GameBattle):

    def valid_guess_given_by_user(self):

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

    def player_alone(self):
        self.generate_board_player_one_to_check()
        self.generate_board_player_one()

        row_bomb, column_bomb = self.valid_position_bomb("aleatory")
        row_ship_two_horizontal, column_ship_two_horizontal = self.valid_position_ship_two_horizontal("aleatory")
        row_ship_two_vertical, column_ship_two_vertical = self.valid_position_ship_two_vertical("aleatory")
        row_ship_three_horizontal, column_ship_three_horizontal = self. valid_position_ship_three_horizontal("aleatory")
        row_ship_three_vertical, column_ship_three_vertical = self.valid_position_ship_three_vertical("aleatory")
        row_ship_four_horizontal, column_ship_four_horizontal = self.valid_position_ship_four_horizontal("aleatory")
        row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship_four_vertical("aleatory")


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
        time.sleep(1)
        self.reset()


        life = 0
        while life <= 10:
            self.print_players("1")
            self.print_board_player_one()
            guess_row, guess_column = self.valid_guess_given_by_user()

            if guess_row == row_bomb and guess_column == column_bomb:
                self.board_player_one[guess_row-1][guess_column-1] = "#"
                self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "A"
                self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] = "A"
                self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] = "B"
                self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] = "B"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "C"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] = "C"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "C"
                self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "E"
                self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] = "F"
                self.reset()
                time.sleep(1)
                print "You have shot to the bomb, and You have sunk all the ships\n"
                self.print_players("1w")
                self.print_board_player_one()
                raw_input("Press -ENTER-")
                self.clean_lists()
                self.reset()
                time.sleep(1)
                self.play_again_alone()

            else:
                if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                    self.reset()
                    time.sleep(1)
                    print "It is not in the ocean\n\n"
                    life +=1
                    print "You still have %d lives, Come on, you can sink the ships" % (10-life)

                elif self.board_player_one[guess_row-1][guess_column-1] == "X" or self.board_player_one[guess_row-1][guess_column-1] == "A"\
                or self.board_player_one[guess_row-1][guess_column-1] == "B" or self.board_player_one[guess_row-1][guess_column-1] == "C"\
                or self.board_player_one[guess_row-1][guess_column-1] == "D" or self.board_player_one[guess_row-1][guess_column-1] == "E"\
                or self.board_player_one[guess_row-1][guess_column-1] == "F":
                    self.reset()
                    time.sleep(1)
                    print "Already You have written those coordinates\n"
                    life +=1
                    print "You still have %d lives, Come on, you can sink the ships" % (10-life)

                elif guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal\
                or guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal+1:
                    self.board_player_one[guess_row-1][guess_column-1] = "A"
                    self.reset()
                    time.sleep(1)

                elif guess_row == row_ship_two_vertical and guess_column == column_ship_two_vertical\
                or guess_row == row_ship_two_vertical+1 and guess_column == column_ship_two_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "B"
                    self.reset()
                    time.sleep(1)

                elif guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+1\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+2:
                    self.board_player_one[guess_row-1][guess_column-1] = "C"
                    self.reset()
                    time.sleep(1)

                elif guess_row == row_ship_three_vertical and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+1 and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+2 and guess_column == column_ship_three_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "D"
                    self.reset()
                    time.sleep(1)

                elif guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+1\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+2\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+3:
                    self.board_player_one[guess_row-1][guess_column-1] = "E"
                    self.reset()
                    time.sleep(1)

                elif guess_row == row_ship_four_vertical and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+1 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+2 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+3 and guess_column == column_ship_four_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "F"
                    self.reset()
                    time.sleep(1)

                else:
                    self.board_player_one[guess_row-1][guess_column-1] = "X"
                    self.reset()
                    time.sleep(1)
                    print "Try again\n"
                    life+=1
                    print "You still have %d lives, Come on, you can sink the ships\n" % (10-life)

            if self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "A" and self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] == "A"\
            and self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] == "B" and self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] == "B"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "C" and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] == "C"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "C" and self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] == "D" and self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] == "E"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "E"\
            and self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] == "F"\
            and self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] == "F":
                self.reset()
                time.sleep(1)
                print "You have sunk all the ships\n"
                self.print_players("1w")
                self.print_board_player_one()
                raw_input("Press -ENTER-")
                self.clean_lists()
                self.reset()
                time.sleep(1)
                self.play_again_alone()

            if life == 10:
                self.reset()
                time.sleep(1)
                print """
__   _____  _   _   _    ___  ___ ___ 
\ \ / / _ \| | | | | |  / _ \/ __| __|
 \ V / (_) | |_| | | |_| (_) \__ \ _| 
  |_| \___/ \___/  |____\___/|___/___|
                                      """
                raw_input("Press -ENTER- ")
                self.reset()
                time.sleep(1)
                self.play_again_alone()

    def play_again_alone(self):

        while True:
            time.sleep(1)
            choose_user = raw_input("Do you want to play again y/n:  ")
            choose_user = choose_user.lower()

            if choose_user == "y":
                self.clean_lists()
                self.reset()
                time.sleep(1)
                self.player_alone()
            elif choose_user == "n":
                self.clean_lists()
                time.sleep(1)
                self.reset()
                self.menu()
            else:
                self.reset()
                time.sleep(1)
                print "Only can write -y- or -n- \n"

class MultiPlayer(SinglePlayer):

    def place_ships_players(self):
        self.generate_board_player_one()
        self.generate_show_board_one()

        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_bomb, column_bomb = self.valid_position_bomb("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_bomb-1][column_bomb-1] = "#"
        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_ship_two_horizontal, column_ship_two_horizontal = self.valid_position_ship_two_horizontal("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "A"
        self.show_board_one[row_ship_two_horizontal-1][column_ship_two_horizontal] = "A"
        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_ship_two_vertical, column_ship_two_vertical = self.valid_position_ship_two_vertical("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_ship_two_vertical-1][column_ship_two_vertical-1] = "B"
        self.show_board_one[row_ship_two_vertical][column_ship_two_vertical-1] = "B"
        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_ship_three_horizontal, column_ship_three_horizontal = self. valid_position_ship_three_horizontal("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "C"
        self.show_board_one[row_ship_three_horizontal-1][column_ship_three_horizontal] = "C"
        self.show_board_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "C"
        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_ship_three_vertical, column_ship_three_vertical = self.valid_position_ship_three_vertical("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_ship_three_vertical-1][column_ship_three_vertical-1] = "D"
        self.show_board_one[row_ship_three_vertical][column_ship_three_vertical-1] = "D"
        self.show_board_one[row_ship_three_vertical+1][column_ship_three_vertical-1] = "D"
        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_ship_four_horizontal, column_ship_four_horizontal = self.valid_position_ship_four_horizontal("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "E"
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal] = "E"
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "E"
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "E"
        self.print_players("b1")
        self.print_show_board_one()
        time.sleep(1)

        row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship_four_vertical("no aleatory one")
        self.reset()
        time.sleep(0)
        self.show_board_one[row_ship_four_vertical-1][column_ship_four_vertical-1] = "F"
        self.show_board_one[row_ship_four_vertical][column_ship_four_vertical-1] = "F"
        self.show_board_one[row_ship_four_vertical+1][column_ship_four_vertical-1] = "F"
        self.show_board_one[row_ship_four_vertical+2][column_ship_four_vertical-1] = "F"
        self.print_players("b1")
        self.print_show_board_one()

        time.sleep(1)
        self.reset()

        print "Now the player two must put his ships\n"
        raw_input("Press -ENTER-")
        time.sleep(1)
        self.reset()

        self.generate_board_player_two()
        self.generate_show_board_two()

        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_bomb2, column_bomb2 = self.valid_position_bomb("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_bomb2-1][column_bomb2-1] = "#"
        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_ship_two_horizontal2, column_ship_two_horizontal2 = self.valid_position_ship_two_horizontal("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2-1] = "A"
        self.show_board_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2] = "A"
        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_ship_two_vertical2, column_ship_two_vertical2 = self.valid_position_ship_two_vertical("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_ship_two_vertical2-1][column_ship_two_vertical2-1] = "B"
        self.show_board_two[row_ship_two_vertical2][column_ship_two_vertical2-1] = "B"
        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_ship_three_horizontal2, column_ship_three_horizontal2 = self. valid_position_ship_three_horizontal("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2-1] = "C"
        self.show_board_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2] = "C"
        self.show_board_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2+1] = "C"
        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_ship_three_vertical2, column_ship_three_vertical2 = self.valid_position_ship_three_vertical("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_ship_three_vertical2-1][column_ship_three_vertical2-1] = "D"
        self.show_board_two[row_ship_three_vertical2][column_ship_three_vertical2-1] = "D"
        self.show_board_two[row_ship_three_vertical2+1][column_ship_three_vertical2-1] = "D"
        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_ship_four_horizontal2, column_ship_four_horizontal2 = self.valid_position_ship_four_horizontal("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2-1] = "E"
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2] = "E"
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+1] = "E"
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+2] = "E"
        self.print_players("b2")
        self.print_show_board_two()
        time.sleep(1)

        row_ship_four_vertical2, column_ship_four_vertical2 = self.valid_position_ship_four_vertical("no aleatory two")
        self.reset()
        time.sleep(0)
        self.show_board_two[row_ship_four_vertical2-1][column_ship_four_vertical2-1] = "F"
        self.show_board_two[row_ship_four_vertical2][column_ship_four_vertical2-1] = "F"
        self.show_board_two[row_ship_four_vertical2+1][column_ship_four_vertical2-1] = "F"
        self.show_board_two[row_ship_four_vertical2+2][column_ship_four_vertical2-1] = "F"
        self.print_players("b2")
        self.print_show_board_two()

#*********************************************************************************************************************

        self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)


    def player_number_one(self, row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2):

        if self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "A" and self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] == "A"\
            and self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] == "B" and self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] == "B"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "C" and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] == "C"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "C" and self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] == "D" and self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] == "E"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "E"\
            and self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] == "F"\
            and self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] == "F":
            self.reset()
            time.sleep(1)
            self.print_players("2w")
            self.print_board_player_one()
            raw_input("\nPress -ENTER- ")
            self.clean_lists()
            self.reset()
            time.sleep(1)
            self.multi_play_again()

        else:
            self.reset()
            time.sleep(1)
            pass

        print "... Your turn. PLAYER 1 ..."

        ask = raw_input("\nDo you want to see your board?  y/n  ")
        ask = ask.lower()
        self.reset()
        time.sleep(1)

        if ask == "y":
            print "\nHere you will see the shots of PLAYER 2\n"
            self.print_board_player_one()
            raw_input("Press -ENTER- ")
            self.reset()
            time.sleep(1)
        else:
            self.reset()
            time.sleep(1)
            pass

        while True:
            self.print_players("1")
            self.print_board_player_two()
            guess_row, guess_column = self.valid_guess_given_by_user()

            if guess_row == row_bomb2 and guess_column == column_bomb2:
                self.board_player_two[guess_row-1][guess_column-1] = "#"
                self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2-1] = "A"
                self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2] = "A"
                self.board_player_two[row_ship_two_vertical2-1][column_ship_two_vertical2-1] = "B"
                self.board_player_two[row_ship_two_vertical2][column_ship_two_vertical2-1] = "B"
                self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2-1] = "C"
                self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2] = "C"
                self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2+1] = "C"
                self.board_player_two[row_ship_three_vertical2-1][column_ship_three_vertical2-1] = "D"
                self.board_player_two[row_ship_three_vertical2][column_ship_three_vertical2-1] = "D"
                self.board_player_two[row_ship_three_vertical2+1][column_ship_three_vertical2-1] = "D"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2-1] = "E"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2] = "E"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+1] = "E"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+2] = "E"
                self.board_player_two[row_ship_four_vertical2-1][column_ship_four_vertical2-1] = "F"
                self.board_player_two[row_ship_four_vertical2][column_ship_four_vertical2-1] = "F"
                self.board_player_two[row_ship_four_vertical2+1][column_ship_four_vertical2-1] = "F"
                self.board_player_two[row_ship_four_vertical2+2][column_ship_four_vertical2-1] = "F"
                self.reset()
                time.sleep(1)
                print "You have shot to the bomb, and You have sunk all the ships\n"
                self.print_players("1w")
                self.print_board_player_two()
                raw_input("Press -ENTER-")
                self.clean_lists()
                self.reset()
                time.sleep(1)
                self.multi_play_again()

            else:
                if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                    self.reset()
                    time.sleep(1)
                    print "It is not in the ocean\n\n"

                elif self.board_player_two[guess_row-1][guess_column-1] == "X" or self.board_player_two[guess_row-1][guess_column-1] == "A"\
                or self.board_player_two[guess_row-1][guess_column-1] == "B" or self.board_player_two[guess_row-1][guess_column-1] == "C"\
                or self.board_player_two[guess_row-1][guess_column-1] == "D" or self.board_player_two[guess_row-1][guess_column-1] == "E"\
                or self.board_player_two[guess_row-1][guess_column-1] == "F":
                    self.reset()
                    time.sleep(1)
                    print "Already You have written those coordinates\n"

                elif guess_row == row_ship_two_horizontal2 and guess_column == column_ship_two_horizontal2\
                or guess_row == row_ship_two_horizontal2 and guess_column == column_ship_two_horizontal2+1:
                    self.board_player_two[guess_row-1][guess_column-1] = "A"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_two_vertical2 and guess_column == column_ship_two_vertical2\
                or guess_row == row_ship_two_vertical2+1 and guess_column == column_ship_two_vertical2:
                    self.board_player_two[guess_row-1][guess_column-1] = "B"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_three_horizontal2 and guess_column == column_ship_three_horizontal2\
                or guess_row == row_ship_three_horizontal2 and guess_column == column_ship_three_horizontal2+1\
                or guess_row == row_ship_three_horizontal2 and guess_column == column_ship_three_horizontal2+2:
                    self.board_player_two[guess_row-1][guess_column-1] = "C"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_three_vertical2 and guess_column == column_ship_three_vertical2\
                or guess_row == row_ship_three_vertical2+1 and guess_column == column_ship_three_vertical2\
                or guess_row == row_ship_three_vertical2+2 and guess_column == column_ship_three_vertical2:
                    self.board_player_two[guess_row-1][guess_column-1] = "D"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_four_horizontal2 and guess_column == column_ship_four_horizontal2\
                or guess_row == row_ship_four_horizontal2 and guess_column == column_ship_four_horizontal2+1\
                or guess_row == row_ship_four_horizontal2 and guess_column == column_ship_four_horizontal2+2\
                or guess_row == row_ship_four_horizontal2 and guess_column == column_ship_four_horizontal2+3:
                    self.board_player_two[guess_row-1][guess_column-1] = "E"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_four_vertical2 and guess_column == column_ship_four_vertical2\
                or guess_row == row_ship_four_vertical2+1 and guess_column == column_ship_four_vertical2\
                or guess_row == row_ship_four_vertical2+2 and guess_column == column_ship_four_vertical2\
                or guess_row == row_ship_four_vertical2+3 and guess_column == column_ship_four_vertical2:
                    self.board_player_two[guess_row-1][guess_column-1] = "F"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                else:
                    self.board_player_two[guess_row-1][guess_column-1] = "X"
                    self.reset()
                    time.sleep(1)
                    print "You have failed"
                    self.print_players("b2")
                    self.print_board_player_two()
                    raw_input("Press -ENTER- ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

    def player_number_two(self, row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2):


        if self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2-1] == "A" and self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2] == "A"\
            and self.board_player_two[row_ship_two_vertical2-1][column_ship_two_vertical2-1] == "B" and self.board_player_two[row_ship_two_vertical2][column_ship_two_vertical2-1] == "B"\
            and self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2-1] == "C" and self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2] == "C"\
            and self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2+1] == "C" and self.board_player_two[row_ship_three_vertical2-1][column_ship_three_vertical2-1] == "D"\
            and self.board_player_two[row_ship_three_vertical2][column_ship_three_vertical2-1] == "D" and self.board_player_two[row_ship_three_vertical2+1][column_ship_three_vertical2-1] == "D"\
            and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2-1] == "E" and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2] == "E"\
            and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+1] == "E" and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+2] == "E"\
            and self.board_player_two[row_ship_four_vertical2-1][column_ship_four_vertical2-1] == "F" and self.board_player_two[row_ship_four_vertical2][column_ship_four_vertical2-1] == "F"\
            and self.board_player_two[row_ship_four_vertical2+1][column_ship_four_vertical2-1] == "F" and self.board_player_two[row_ship_four_vertical2+2][column_ship_four_vertical2-1] == "F":
            self.reset()
            time.sleep(1)
            self.print_players("1w")
            self.print_board_player_two()
            raw_input("Press -ENTER-")
            self.clean_lists()
            self.reset()
            time.sleep(1)
            self.multi_play_again()
        else:
            self.reset()
            time.sleep(1)
            pass

        print "... Your turn. PLAYER 2 ..."

        ask = raw_input("\nDo you want to see your board?  y/n  ")
        ask = ask.lower()
        self.reset()
        time.sleep(1)

        if ask == "y":
            print "\nHere you will see the shots of PLAYER 1\n"
            self.print_board_player_two()
            raw_input("Press -ENTER- ")
            self.reset()
            time.sleep(1)
        else:
            self.reset()
            time.sleep(1)
            pass

        while True:
            self.print_players("2")
            self.print_board_player_one()
            guess_row, guess_column = self.valid_guess_given_by_user()

            if guess_row == row_bomb and guess_column == column_bomb:
                self.board_player_one[guess_row-1][guess_column-1] = "#"
                self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "A"
                self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] = "A"
                self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] = "B"
                self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] = "B"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "C"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] = "C"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "C"
                self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "E"
                self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] = "F"
                self.reset()
                time.sleep(1)
                print "You have shot to the bomb, and You have sunk all the ships\n"
                self.print_players("2w")
                self.print_board_player_one()
                raw_input("\nPress -ENTER- ")
                self.clean_lists()
                self.reset()
                time.sleep(1)
                self.multi_play_again()
            else:
                if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                    self.reset()
                    time.sleep(1)
                    print "It is not in the ocean\n\n"

                elif self.board_player_one[guess_row-1][guess_column-1] == "X" or self.board_player_one[guess_row-1][guess_column-1] == "A"\
                or self.board_player_one[guess_row-1][guess_column-1] == "B" or self.board_player_one[guess_row-1][guess_column-1] == "C"\
                or self.board_player_one[guess_row-1][guess_column-1] == "D" or self.board_player_one[guess_row-1][guess_column-1] == "E"\
                or self.board_player_one[guess_row-1][guess_column-1] == "F":
                    self.reset()
                    time.sleep(1)
                    print "Already You have written those coordinates\n\n"

                elif guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal\
                or guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal+1:
                    self.board_player_one[guess_row-1][guess_column-1] = "A"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_two_vertical and guess_column == column_ship_two_vertical\
                or guess_row == row_ship_two_vertical+1 and guess_column == column_ship_two_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "B"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+1\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+2:
                    self.board_player_one[guess_row-1][guess_column-1] = "C"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_three_vertical and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+1 and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+2 and guess_column == column_ship_three_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "D"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+1\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+2\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+3:
                    self.board_player_one[guess_row-1][guess_column-1] = "E"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif guess_row == row_ship_four_vertical and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+1 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+2 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+3 and guess_column == column_ship_four_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "F"
                    self.reset()
                    time.sleep(1)
                    print "You have shot to a part of one ship"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                else:
                    self.board_player_one[guess_row-1][guess_column-1] = "X"
                    self.reset()
                    time.sleep(1)
                    print "You have failed"
                    self.print_players("b1")
                    self.print_board_player_one()
                    raw_input("Press -ENTER- ")
                    self.player_number_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

    def multi_play_again(self):

        while True:
            time.sleep(1)
            choose_user = raw_input("Do you want to play again y/n:  ")
            choose_user = choose_user.lower()

            if choose_user == "y":
                self.clean_lists()
                self.reset()
                time.sleep(1)
                self.place_ships_players()
            elif choose_user == "n":
                self.clean_lists()
                time.sleep(1)
                self.reset()
                self.menu()
            else:
                self.reset()
                time.sleep(1)
                print "Only can write -y- or -n- \n"

    def instructions(self):
        print """
 ___           _                   _   _                 
|_ _|_ __  ___| |_ _ __ _   _  ___| |_(_) ___  _ __  ___ 
 | || '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|
 | || | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \ 
|___|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/
                                                         """

        print "Single Player:"
        print "\nWhen you guess right the position of one part of the ship"
        print "will appear one of these symbols -A- -B- -C- -D- -E- -F-"
        print "when you do not guess right, will appear this symbol -X-"
        print "when you shoot to the bomb, will appear this symbol -#-"
        print "and you will win automatically"
        print "You have 10 lives"

        print "\nMulti Player: "
        print "When one of you guess right the position of one part of the ship"
        print "will appear one of these symbols -A- -B- -C- -D- -E- -F-"
        print "when one of you do not guess right, will appear this symbol -X-"
        print "when one of you shoot to the bomb, will appear this symbol -#-"
        print "and one of you will win automatically"

        raw_input("\nPress -ENTER- to return the menu")
        self.reset()
        self.menu()

    def menu_print(self):
        """This saves the instructions of the game"""

        print "Welcome to Battleship"
        print "\nChoose an option that you want"
        print "\n 1. Single Player"
        print "\n 2. Two Players"
        print "\n 3. Instructions"
        print "\n 4. Exit"

    def menu_option(self):
        """This saves the election of the user"""

        while True:

            choose_user = raw_input(" - ")

            if choose_user == "1":
                self.reset()
                self.player_alone()

            elif choose_user == "2":
                self.reset()
                self.place_ships_players()

            elif choose_user == "3":
                self.reset()
                self.instructions()

            elif choose_user == "4":
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


MAIN = MultiPlayer()
MAIN.menu()