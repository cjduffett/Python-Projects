import sys
from Maze import Maze

# ----------------------------------------------
# Evaluates a set of mazes given an inout file
# ----------------------------------------------

class MazeController:

    def __init__(self):

        self.num_mazes = 0
        self.mazes = list()

    '''
        Read the input file and pass the solver instructions
        to each maze object
    '''    
    def readMazeFile(self, filename):

        f = open(filename)
        self.num_mazes = int(f.readline())

        for i in range(0, self.num_mazes):
            dir_list = f.readline().split()
            self.mazes.append(Maze(dir_list[0], dir_list[1]))

        f.close()
        
    def writeMazeFile(self, filename):
        
        w = open(filename,'w')
        
        for i in range(0, self.num_mazes):
            
            w.write("Case #" + str(i + 1) + ":\n")
            
            xmin, xmax, ymin, ymax = self.mazes[i].getRange()
            
            for y in range(ymin,ymax + 1):
        
                for x in range(xmin,xmax + 1):
                
                    w.write(self.mazes[i].rooms[(x,y)].getState())
                
                w.write("\n")
                
        w.close()

    '''
        Solve the list of input mazes
    '''
    def solve(self):

        for maze in self.mazes:

            maze.solveForward()
            maze.solveBackward()
            maze.evalMaze()
