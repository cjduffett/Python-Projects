import sys

# ----------------------------------------------
# Boundaries of the maze; min/max x and y vals
# ----------------------------------------------

class Boundaries:

    def __init__(self):

        self.xmin = 0
        self.ymin = 0
        self.xmax = 0
        self.ymax = 0

    
    def getSize(self):

        return int(abs(self.ymax - self.ymin) + 1), int(abs(self.xmax - self.xmin) + 1) # row, cols
        
    def getRange(self):
        
        return self.xmin, self.xmax, self.ymin, self.ymax
        
    def printIt(self):
        
        sys.stdout.write("(" + str(self.xmin) + ", " + str(self.xmax))
        sys.stdout.write(", " + str(self.ymin) + ", " + str(self.ymax) + ")\n")
