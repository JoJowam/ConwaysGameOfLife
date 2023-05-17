import os
from tkinter import *
from PIL import Image, ImageTk


class GameOfLifeGUI:
    def __init__(self, master, width, height, board):

        self.master = master
        self.width = width
        self.height = height
        self.board = board
        self.square_size = 20
        self.line_width = 0.5

        self.master.title("Conway's Game of Life")
        self.master.geometry("1280x800")
        self.master.resizable(False, False)

        self.canvas = Canvas(master, width=1060, height=706)
        self.canvas.place(x=14, y=83)

        self.draw_board()

        self.speed_scale = Scale(master, from_=1, to=10, orient=HORIZONTAL, bg="#ffcbdb",
                                 fg="white", width=15, font="Arial 12 bold")
        self.speed_scale.set(5)
        self.speed_scale.place(x=1100, y=88)

        self.scale = Scale(master, from_=10, to=50, orient=HORIZONTAL, command=self.zoom_board, bg="#ffcbdb",
                           fg="white", width=15, font="Arial 12 bold")
        self.scale.set(self.square_size)
        self.scale.place(x=1100, y=172)

        self.start_button = Button(master, text="START", command=self.start_game, bg="#ffcbdb", fg="white", width=15,
                                   height=1, font="Arial 12 bold")
        self.start_button.place(x=1100, y=276)

    def zoom_board(self, value):
        self.square_size = int(value)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        self.canvas.configure(bg="#FFCBDB")
        self.create_lines()
        for i in range(self.width):
            for j in range(self.height):
                if self.board.board[i][j] == 1:
                    x0, y0 = i * self.square_size, j * self.square_size
                    x1, y1 = x0 + self.square_size, y0 + self.square_size
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="#FF5733")

    def create_lines(self):
        for i in range(self.width):
            self.canvas.create_line(i * self.square_size, 0, i * self.square_size, self.height * self.square_size,
                                    fill="white", width=self.line_width)
        for j in range(self.height):
            self.canvas.create_line(0, j * self.square_size, self.width * self.square_size, j * self.square_size,
                                    fill="white", width=self.line_width)

    def start_game(self):
        def update():
            self.board.define_next_generation()
            self.draw_board()
            speed = 1000 // self.speed_scale.get()
            self.master.after(speed, update)

        self.start_button.config(state=DISABLED)
        self.scale.config(state=DISABLED)
        update()
