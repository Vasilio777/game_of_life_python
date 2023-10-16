import turtle
from Board import Board
from constants import screensize

class BoardDrawer(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.cell_size = 22
        self.board = Board()
        self.gird_offset_x = self.board.height*self.cell_size / 2
        self.gird_offset_y = self.board.width*self.cell_size / 2
        
        self.draw()

    def draw(self):
        # firstly, iterate height (avoid non-square grid errors) 
        for i in range(self.board.height):
            for j in range(self.board.width):
                self.setpos(i*self.cell_size - self.gird_offset_x, j*self.cell_size - self.gird_offset_y)
                if self.board.get_cell_state(i, j):
                    self.color('black')
                else:
                    self.color('gray')
                self.stamp()

    def render(self):
        self.clear()
        self.board.update_alive()
        self.draw()

    def toggle_cell_state(self, x, y):
        new_x = round((x + self.gird_offset_x)/self.cell_size)
        new_y = round((y + self.gird_offset_y)/self.cell_size)

        if new_x in range(self.board.height) and \
            new_y in range(self.board.width):
            self.board.set_cell_state(new_x, new_y)
            self.draw()