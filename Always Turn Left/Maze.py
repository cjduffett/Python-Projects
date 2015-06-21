import sys
from Coordinate import Coordinate
from Boundaries import Boundaries
from Room import Room

# ----------------------------------------------
# Single complete maze
# ----------------------------------------------

class Maze:

    def __init__(self, fwd_instructions, rev_instructions):

        self.fwd_instructions = fwd_instructions
        self.rev_instructions = rev_instructions

        self.bounds = Boundaries()
        self.curr_pos = Coordinate(0,0) # current position
        self.curr_dir = 's' # current direction
        
        self.rooms = {}
        self.rooms[(0,0)] = Room(Coordinate(0,0))
        self.rooms[(0,0)].clearNorthWall()
        
        self.entrance = Coordinate(0,0)
        self.exit = None

    '''
        Solve the maze following the directions forward. Should be executed
        Before solveBackward() is executed.
    '''
    def solveForward(self):
        
        for step in self.fwd_instructions[1:len(self.fwd_instructions) - 1]: # skip first/last W
            
            if (self.isWalking(step)):

                if (self.facingNorth()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearNorthWall()
                    self.curr_pos.y -= 1

                    # create new room
                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))

                    # clear the wall that was just crossed
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearSouthWall()

                elif (self.facingEast()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearEastWall()
                    self.curr_pos.x += 1

                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearWestWall()

                elif (self.facingSouth()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearSouthWall()
                    self.curr_pos.y += 1

                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearNorthWall()

                elif (self.facingWest()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearWestWall()
                    self.curr_pos.x -= 1

                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearEastWall()

                self.updateBoundaries()

            else:

                # change direction
                self.turn(step)

        # end for

        # process last step out of the maze
        if (self.facingNorth()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearNorthWall()

        elif (self.facingEast()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearEastWall()

        elif (self.facingSouth()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearSouthWall()

        elif (self.facingWest()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearWestWall()

        self.exit = Coordinate(self.curr_pos.x,self.curr_pos.y)
        self.ending_d = self.curr_dir        
    
    '''
        Solve the maze following the directions in reverse. Reveals any remaining
        maze tiles that were not vistied when solved forward.
    '''
    def solveBackward(self):
        
        self.curr_pos = self.exit  # start at the exit
        self.turn('R')      # setup to reverse direction
        self.turn('R')
        
        for step in self.rev_instructions[1:len(self.rev_instructions) - 1]: # skip first/last W
            
            if (self.isWalking(step)):

                if (self.facingNorth()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearNorthWall()
                    self.curr_pos.y -= 1

                    # create new room
                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))

                    # clear the wall that was just crossed
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearSouthWall()

                elif (self.facingEast()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearEastWall()
                    self.curr_pos.x += 1

                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearWestWall()

                elif (self.facingSouth()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearSouthWall()
                    self.curr_pos.y += 1

                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearNorthWall()

                elif (self.facingWest()):
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearWestWall()
                    self.curr_pos.x -= 1

                    if (self.curr_pos.x,self.curr_pos.y) not in self.rooms:
                        self.rooms[(self.curr_pos.x,self.curr_pos.y)] = Room(Coordinate(self.curr_pos.x,self.curr_pos.y))
                    
                    self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearEastWall()

                self.updateBoundaries()

            else:

                # change direction
                self.turn(step)

        # end for

        # process last step out of the maze
        if (self.facingNorth()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearNorthWall()

        elif (self.facingEast()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearEastWall()

        elif (self.facingSouth()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearSouthWall()

        elif (self.facingWest()):
            self.rooms[(self.curr_pos.x,self.curr_pos.y)].clearWestWall()

        self.exit = Coordinate(self.curr_pos.x,self.curr_pos.y)
        self.ending_d = self.curr_dir            

    '''
        Update the current boundaries of the maze
    '''
    def updateBoundaries(self):

        if (self.curr_pos.x > self.bounds.xmax):
            self.bounds.xmax = self.curr_pos.x

        if (self.curr_pos.x < self.bounds.xmin):
            self.bounds.xmin = self.curr_pos.x

        if (self.curr_pos.y > self.bounds.ymax):
            self.bounds.ymax = self.curr_pos.y

        if (self.curr_pos.y < self.bounds.ymin):
            self.bounds.ymin = self.curr_pos.y        

    '''
        Return the size of the maze
    '''
    def getSize(self):
        return self.bounds.getSize()
    
    '''
        Returns the minimum and maximum x and y values of the boundaries
    '''    
    def getRange(self):
        return self.bounds.getRange()

    '''
        Checks if the current direction the solver is facing a given direction
    '''
    def facingNorth(self):
        return self.curr_dir == 'n'

    def facingEast(self):
        return self.curr_dir == 'e'

    def facingSouth(self):
        return self.curr_dir == 's'

    def facingWest(self):
        return self.curr_dir == 'w'

    '''
        Check if the current step in the instructions is a walking step
    '''
    def isWalking(self, step):
        return step == 'W'
    
    '''
        Handle a turning step in the instructions. Rotate solver
        CW or CCW by 90 degrees.
    '''
    def turn(self, step):

        if (step == 'R'):

            # right; clockwise
            
            if (self.curr_dir == 'n'):
                self.curr_dir = 'e'

            elif (self.curr_dir == 'e'):
                self.curr_dir = 's'

            elif (self.curr_dir == 's'):
                self.curr_dir = 'w'

            elif (self.curr_dir == 'w'):
                self.curr_dir = 'n'

        else:
            
            # left; counterclockwise
            
            if (self.curr_dir == 'n'):
                self.curr_dir = 'w'
                
            elif (self.curr_dir == 'w'):
                self.curr_dir = 's'
                
            elif (self.curr_dir == 's'):
                self.curr_dir = 'e'

            elif (self.curr_dir == 'e'):
                self.curr_dir = 'n' 
    
    '''
        Scan each room in the maze after exploration is complete
        and determine the state of each room. Valid states are (1 - f):
        
        0 - All walls blocked (Invalid when graded, used only internally)
        1 - North wall clear
        2 - South wall clear
        3 -
        4 -
        ...
        d -
        e - 
        f - All walls clear 
    '''
    def evalMaze(self):
        
        xmin,xmax,ymin,ymax = self.getRange()
        
        for y in range(ymin,ymax + 1):
        
            for x in range(xmin,xmax + 1):
                
                self.rooms[(x,y)].genState()
