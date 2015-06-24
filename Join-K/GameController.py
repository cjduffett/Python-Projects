__author__ = 'cjduffett'

from Game import Game

# ----------------------------------------------
# Evaluates a set of game boards given an input file
# ----------------------------------------------

class GameController:

    def __init__(self):

        self.num_games = 0
        self.games = list()

    '''
        Read the input file and pass the game board to each game object
    '''

    def readInputFile(self, filename):

        f = open(filename)
        self.num_games = int(f.readline())

        for i in range(0, self.num_games):

            params = f.readline().split()
            board_size = params[0]
            row_size = params[1]
            self.games.append(Game(board_size, row_size))

            for j in range(0, board_size):

                # build row list
                row = f.readline().split()
                self.games[i].rows.append(row)

                # build column list
                for k in range(0, board_size):
                    self.games[i].cols.append([row[i]])

                # for
            # for
        # for

    '''
        Write the solved game boards to an output file
    '''

    def writeOutputFile(self, filename):

        f = open(filename)

        for i in range(0, self.num_games):

            game = self.games[i]
            f.write("Case #" + str(i + 1) + ": ")
            f.write(game.result + "\n")

        # for

    '''
        solve each of the game boards
    '''

    def solve(self):

        for i in range(0, self.num_games):

            self.games[i].solve()

        # for