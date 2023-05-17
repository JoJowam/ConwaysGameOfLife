class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(width)] for y in range(height)]

    def alive(self, x, y):
        self.board[x][y] = 1

    def dead(self, x, y):
        self.board[x][y] = 0

    def have_neighbors(self, x, y):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < self.width and 0 <= y + j < self.height:
                    neighbors.append(self.board[y + j][x + i])
        return neighbors

    def is_neighbor_alive(self, x, y):
        neighbors = self.have_neighbors(x, y)
        return sum(neighbors)

    def define_next_generation(self):
        next_board = [[0 for x in range(self.width)] for y in range(self.height)]

        for i in range(self.width):
            for j in range(self.height):
                alive_neighbors = self.is_neighbor_alive(i, j)
                if self.board[j][i] and (alive_neighbors == 2 or alive_neighbors == 3):
                    next_board[j][i] = 1
                elif not self.board[j][i] and alive_neighbors == 3:
                    next_board[j][i] = 1
        self.board = next_board

    def reset_board(self):
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]