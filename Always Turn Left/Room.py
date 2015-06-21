import sys
import Coordinate

# ----------------------------------------------
# Single maze room (tile in the maze)
# ----------------------------------------------
class Room:

    def __init__(self, coordinate):

        self.coord = coordinate
        self.state = 0 # assume can't go anywhere
        self.n_clear = False
        self.e_clear = False
        self.s_clear = False
        self.w_clear = False

    '''
        Updates the current state of the room (0 - 15) based on which
        walls are cleared
    '''
    def genState(self):
        
        if self.n_clear:
            self.state += 1
        
        if self.s_clear:
            self.state += 2
            
        if self.w_clear:
            self.state += 4
            
        if self.e_clear:
            self.state += 8
    
    '''
        Returns a hexidecimal number that represents the state
        (which walls are clear) of each room in the maze
    '''
    def getState(self):

        # returns string in hexadecimal format (1 - f)
        
        return format(self.state,'x')
       
    '''
        Prints the single state character (no leading/trailing whitespace)
    ''' 
    def printState(self):
        
        sys.stdout.write(format(self.state,'x'))

    '''
        Adjusts the state value (0 - 15) of the room as walls
        are crossed
    '''
    def clearNorthWall(self):
        self.n_clear = True

    def clearEastWall(self):
        self.e_clear = True

    def clearSouthWall(self):
        self.s_clear = True

    def clearWestWall(self):
        self.w_clear = True
