__author__ = 'cjduffett'

from GameController import GameController

sizes = ["small", "large"]

for size in sizes:

    G = GameController()
    G.readInputFile("A-" + size + "-practice.in")
    G.solve()
    G.writeOutputFile("A-" + size + "-practice.out")

# for
