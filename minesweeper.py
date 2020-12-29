# David Lee
# CS 325 Portfolio Project - NP Problems (Minesweeper)

#####################################################################################
###################################### Sources ######################################
#####################################################################################
# Journal article for choosing NP-Complete Game
# 1. Kendall, Graham, Parkes, Andrew, and Spoerer, Kristian.
#    ‘A SURVEY OF NP-COMPLETE PUZZLES’. 1 Jan. 2008 : 13 – 34.
# 2. Kaye, Richardd. “Minesweeper Is NP-Complete.” Springer-Verlag,
#    vol. 22, no. 2, 2000, pp. 9–15.,
#    www.minesweeper.info/articles/MinesweeperIsNPComplete.pdf.

# General ideas on how to build the project adapted from:
#    https://www.askpython.com/python/examples/create-minesweeper-using-python
#    https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de

# Idea of focusing on 3x3 grid instead of iterating over entire m*n board adapted from:
#    https://www.youtube.com/watch?v=ptMMa-SDSeE


#####################################################################################
#################################### Minesweeper ####################################
#####################################################################################

# import os
import sys
import random

class Minefield:
    """
    Initializes and sets up Minesweeper playing field
    Two boards: Public (Player's Visible board) as String type and Private (Actual, hidden board) as Integer type
    """

    def __init__(self):
        self.board = [['-' for i in range(9)] for j in range(9)]
        self._board = [[0 for i in range(9)] for j in range(9)]
        self.mine_map = {}

    def print_field(self):
        """
        Prints out the field viewable to the player
        """

        board_index = iter(range(1, 10))
        print('  1 2 3 4 5 6 7 8 9')
        for row in self.board:
            print(next(board_index), end=' ')
            print(' '.join(row))

    def combine_boards(self):
        for row in range(9):
            for column in range(9):
                exchange = str(self._board[row][column])
                self.board[row][column] = exchange

                if self._board[row][column] == -1:
                    self.board[row][column] = '*'

        self.print_field()

    def mine_locations(self):
        """
        Use Random module to place 10 mines within 9x9 square onto hidden board
        Places mines onto public (player's viewable) board
        """

        num_mines = 0

        while num_mines < 10:
            # 0,8 since randint takes 8 as inclusive; playing on a 9x9 grid with index starting at 0
            row = random.randint(0, 8)
            column = random.randint(0, 8)

            if self._board[row][column] == 0:
                self._board[row][column] = -1
                self.mine_map[(row, column)] = -1
                num_mines += 1

    def cell_value(self):
        """
        Calculate value of individual cells
        """

        # Iterates through each mine and finds each mine location
        for mine in self.mine_map:
            (mine_row, mine_column) = mine

            # Create a 3x3 grid around the mine location (end value +2 because range() is exclusive)
            for i in range(mine_row - 1, mine_row + 2):
                for j in range(mine_column - 1, mine_column + 2):

                    # Assess cell is valid and within the 9x9 square
                    if 0 <= i < 9:
                        if 0 <= j < 9:

                            # Increment value of cell adjacent to mines
                            if self._board[i][j] != -1:
                                self._board[i][j] += 1
        return self._board


class Minesweeper(Minefield):
    def __init__(self):
        Minefield.__init__(self)
        self.current_input = []
        self.game_over = False

    def ask_input(self):
        """
        Verifies player's input is valid and then saves player's input into `current_input` array
        """

        valid_response = False
        while not valid_response:
            player_input = input("Enter row and column number separated by a comma: ")

            if "," not in player_input:
                print("Invalid input. Try again. ")

            else:
                # Format to erase extra spaces and separate input values into row/column
                player_input = player_input.replace(" ", "").split(",")
                player_row = int(player_input[0])
                player_column = int(player_input[1])
                # Adjust for zero index based counting
                player_row -= 1
                player_column -= 1

                if 0 <= player_row < 9 and 0 <= player_column < 9:
                    self.current_input.append(player_row)
                    self.current_input.append(player_column)
                    valid_response = True

                else:
                    print("Invalid input. Try again. ")

    def find_neighbors(self, row, column):
        """
        Method performed after explore_cell. Cell is pre-checked for validity and is not a mine
        Utilize similar flood fill algorithm limited to 3x3 grid to recursively find zero value neighbors
        """

        exchange = str(self._board[row][column])
        self.board[row][column] = exchange

        # flood fill/bucket fill targeting hidden 0-value cells within board boundaries
        if self._board[row][column] == 0:
            for x in range(row - 1, row + 2):
                if x < 0 or x > 8:
                    continue

                for y in range(column - 1, column + 2):
                    if y < 0 or y > 8:
                        continue

                    elif self.board[x][y] != '-':
                        continue

                    else:
                        self.find_neighbors(x, y)

    def game_status(self):
        """
        Checks status of the game to see if player won the game
        """

        cells_checked = 0
        for row in range(9):
            for column in range(9):
                if self.board[row][column] != '-':
                    cells_checked += 1

        if cells_checked == 71:
            self.clear_screen()
            print("\n Congrats, you win!")
            self.restart_game()
            return True

        return False

    def clear_screen(self):
        """
        Method to make room from previous prints to terminal space
        """

        print ("\n" * 5)

        # Old method : still brings up errors
        # try:
        #     os.system('clear')
        # except:
        #     os.system('cls')

    def explore_cell(self):
        """
        Takes player's input and checks to see if player's move results in loss or exploration of the cell
        """

        inputrow = self.current_input.pop(0)
        inputcolumn = self.current_input.pop(0)

        if (inputrow, inputcolumn) in self.mine_map.keys():
            self.clear_screen()
            print(f"Your choice {inputrow + 1},{inputcolumn + 1} was a mine! Game Over")
            self.game_over = True
            self.restart_game()

        elif self.board[inputrow][inputcolumn] != '-':
            self.clear_screen()
            print(f"Your choice {inputrow + 1},{inputcolumn + 1} is already explored. Try again! ")

        else:
            self.find_neighbors(inputrow, inputcolumn)

    def play(self):
        """
        Central game loop
        """

        self.mine_locations()
        self._board = self.cell_value()
        game_finished = False

        while not game_finished:
            self.clear_screen()
            self.print_field()
            self.ask_input()
            self.explore_cell()

            if self.game_over:
                break

            if self.game_status():
                game_finished = True

    def restart_game(self):
        """
        Display to user when game is over
        """

        playerinput = input("\n Enter 'y' to play again. "
                            "\n Enter 'b' to view the board. "
                            "\n Enter any other key to quit. ")

        if playerinput == 'y':
            self.setup()

        elif playerinput == 'b':
            self.combine_boards()
            self.restart_game()

        else:
            sys.exit()

    def setup(self):
        newgame = Minesweeper()
        newgame.play()


if __name__ == '__main__':
    newgame = Minesweeper()
    newgame.setup()