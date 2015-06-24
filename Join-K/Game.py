__author__ = 'cjduffett'

from GameBoard import GameBoard

# ----------------------------------------------
# Individual game of Join-K
# ----------------------------------------------

class Game:

    def __init__(self, board_size, row_size):

        self.result = "Neither"
        self.game_board = GameBoard(board_size)

    '''
        Check if the specified pawn color has a winning position
    '''

    def checkForWin(self, color):

        c = color # R, B

    '''
        Rotate the game board 90 degrees clockwise
    '''

    def rotateClockwise90(self):

        self.game_board.rotateClockwise90()

