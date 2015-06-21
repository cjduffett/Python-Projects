import sys

# ----------------------------------------------
# Cartesian coordinate point
# ----------------------------------------------

class Coordinate:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        
    def printIt(self):
        
        sys.stdout.write("(" + str(self.x) + ", " + str(self.y) + ")")
