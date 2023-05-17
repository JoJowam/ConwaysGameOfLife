from tkinter import *

from board import Board
from gui import GameOfLifeGUI


def run():
    width = 200;
    height = 200;
    board = Board(width, height)
    board.alive(4, 5)
    board.alive(5, 5)
    board.alive(6, 4)
    board.alive(6, 5)
    board.alive(6, 6)

    root = Tk()
    game = GameOfLifeGUI(root, width, height, board)

    root.mainloop()
