# MAZE SOLVER
# ==============================================
# Google Code Jam 2008: Always Turn Left
# Carlton Duffett

from MazeController import MazeController

# ----------------------------------------------
# main script
# ----------------------------------------------

sizes = ["small","large"]

for size in sizes:

    M = MazeController()
    M.readMazeFile("B-" + size + "-practice.in")
    M.solve()
    M.writeMazeFile("B-" + size + "-practice.out")
