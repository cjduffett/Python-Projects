__author__ = 'cjduffett'

import library

from OtherClass import OtherClass

# ----------------------------------------------
# Class description
# ----------------------------------------------

class GameBoard:

    def __init__(self, board_size):

        self.size = board_size
        self.rows = list()
        self.cols = list()

    '''
        Read the input file and pass the solver instructions
        to each maze object
    '''

    def aFunction(self):
        print self.foo