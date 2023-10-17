import random 

class Board():
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 30
        self.board = []
        for _ in range(self.height):
            self.board.append([False]*self.width)

        
        self.still_lifes = {
            'Block':[
                [True,True],
                [True,True]
            ],
            'Bee-hive':[
                [],
                [],
                [],
            ],
            'Tub':[
                [False,True,False],
                [True,False,True],
                [False,True,False]
            ]
        }

        self.fill_random()


    def scan_field(self):
        i, j = 1, 1
        figure_size = self.get_still_life(i, j)
        if figure_size > 1:
            # print(figure_size)
            figure = []
            has_extra_values = False

            for k in range(figure_size):
                # if has_extra_values:
                #     break

                figure_row = []
                for l in range(figure_size):
                    if (i + k - 1 >= 0 and j + l - 1 >= 0 and
                        self.get_cell_state(i + k - 1, j + l - 1)):
                        has_extra_values = True
                        # break

                    cell_state = self.get_cell_state(i + k, j + l)
                    figure_row.append(cell_state)
                figure.append(figure_row)
            print((i, j), figure_size, figure)
        # for i in range(self.width):
        #     for j in range(self.height):
        #         figure_size = self.get_still_life(i, j)
        #         if figure_size > 1:
        #             # print(figure_size)
        #             figure = []
        #             has_extra_values = False

        #             for k in range(figure_size):
        #                 if has_extra_values:
        #                     break

        #                 figure_row = []
        #                 for l in range(figure_size):
        #                     if (i + k - 1 >= 0 and j + l - 1 >= 0 and
        #                         self.get_cell_state(i + k - 1, j + l - 1)):
        #                         has_extra_values = True
        #                         break

        #                     cell_state = self.get_cell_state(i + k, j + l)
        #                     figure_row.append(cell_state)
        #                 figure.append(figure_row)
        #             print((i, j), figure_size, figure)

                    #---
                    # for k in range(-1, figure_size):
                    #     figure_row = []
                    #     for l in range(-1, figure_size):
                    #         figure_row.append(self.get_cell_state(i + k , j + l))
                    #     figure.append(figure_row)
                    # if True not in figure[0] and True not in [t[0] for t in figure]:
                    #     figure = figure[1:]
                    #     for p in range(len(figure)):
                    #         figure[p] = figure[p][1:]
                    #---
                    # if not has_extra_values:
                    #     # print((i, j), figure_size, figure)
                    #     for val, key in zip(self.still_lifes.values(), self.still_lifes.keys()):
                    #         if val == figure:
                    #             print(key)

    def get_still_life(self, x, y) -> int:
        checked_cells = set()
        depth = 1

        while depth < 10:
            alive_counter = 0
            for x_ in range(max(0, x), min(self.width, x + depth + 1)):
                for y_ in range(max(0, y), min(self.height, y + depth + 1)):
                    if (x_, y_) not in checked_cells and self.board[x_][y_]:
                        alive_counter += 1
                        checked_cells.add((x_, y_))
            if alive_counter > 0:
                depth += 1
            else:
                break

        return depth if depth < 10 else -1

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

    def fill_random(self):
        self.set_cell_state(4, 1)
        self.set_cell_state(4, 2)
        self.set_cell_state(5, 1)
        self.set_cell_state(5, 2)

        self.set_cell_state(2, 1)
        self.set_cell_state(1, 2)
        self.set_cell_state(2, 3)
        self.set_cell_state(3, 2)

        self.set_cell_state(12, 11)
        self.set_cell_state(11, 12)
        self.set_cell_state(12, 13)
        self.set_cell_state(13, 12)

        self.set_cell_state(15, 5)
        self.set_cell_state(15, 6)
        self.set_cell_state(16, 5)
        self.set_cell_state(16, 6)

        # fill_size = 5
        # range_w = range(int(self.width / 2 - fill_size / 2), int(self.width / 2 + fill_size / 2))
        # range_h = range(int(self.height / 2 - fill_size / 2), int(self.height / 2 + fill_size / 2))
        # for i in range_w:
        #     for j in range_h:
        #         if bool(random.getrandbits(1)):
        #             self.set_cell_state(i, j)
        
        self.scan_field() # DEBUG

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
