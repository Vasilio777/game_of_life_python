class Board():
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 20
        self.board = []
        for _ in range(self.height):
            self.board.append([False]*self.width)

    def get_cell_destiny(self, x, y):
        alive_counter = 0
        for x_ in range(max(0,x-1),min(self.height,x+2)):
            for y_ in range(max(0,y-1),min(self.width,y+2)):
                if (x,y)==(x_,y_): continue
                if self.board[x_][y_]:
                    alive_counter += 1
        return alive_counter

    def get_cell_state(self, x, y):
        return self.board[x][y]

    def set_cell_state(self, x, y):
        self.board[x][y] = not self.board[x][y]

    def update_alive(self):
        cache = self.board.copy()
        for row in range(len(self.board)):
            cache_row = self.board[row].copy()
            for col in range(len(self.board[row])):
                cell_destiny = self.get_cell_destiny(row, col)
                if cell_destiny < 2:
                    cache_row[col] = False
                elif cell_destiny == 3:
                    cache_row[col] = True
                elif cell_destiny > 3:
                    cache_row[col] = False
            cache[row] = cache_row

        self.board = cache
