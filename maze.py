import time
import random
from cell import Cell


class Maze:
    def __init__(
            self, x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win, seed=0
            ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        random.seed(seed)
    

    def _create_cells(self):
        cells = []
        for r in range(self._num_rows):
            curr_row = []
            for c in range(self._num_cols):
                start_x = self._x1 + c * self._cell_size_x
                start_y = self._y1 + r * self._cell_size_y

                cell = Cell(
                        start_x, start_y, 
                        start_x + self._cell_size_x, 
                        start_y + self._cell_size_y,
                        self._win
                        )
                curr_row.append(cell)

            cells.append(curr_row)
        self._cells = cells
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                self._draw_cell(i, j, 0)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j, sleep_time=0.05):
        self._cells[i][j].draw()
        self._animate(sleep_time)

    def _animate(self, sleep_time):
        self._win.redraw()
        time.sleep(sleep_time)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = []
            if i > 0 and self._cells[i-1][j].visited == False:
                directions.append((i-1, j))
            if i < self._num_rows - 1 and self._cells[i+1][j].visited == False:
                directions.append((i+1, j))
            if j > 0 and self._cells[i][j-1].visited == False:
                directions.append((i, j-1))
            if j < self._num_cols - 1 and self._cells[i][j+1].visited == False:
                directions.append((i, j + 1))
            if len(directions) == 0:
                break
            curr_dir = random.choice(directions)
            if curr_dir[0] == i:
                if curr_dir[1] > j:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][j+1].has_left_wall = False
                else:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][j-1].has_right_wall = False
            elif curr_dir[0] > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i+1][j].has_top_wall = False
            else:
                self._cells[i][j].has_top_wall = False
                self._cells[i-1][j].has_bottom_wall = False
            self._draw_cell(i, j)
                
            self._break_walls_r(curr_dir[0], curr_dir[1])


    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._cells[i][j].visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        up = self._cells[i][j].has_top_wall == False
        down = self._cells[i][j].has_bottom_wall == False
        left = self._cells[i][j].has_left_wall == False
        right = self._cells[i][j].has_right_wall == False
        while True:
            directions = []
            if i > 0 and up and self._cells[i-1][j].visited == False:
                directions.append((i-1, j))
            if i < self._num_rows and down and self._cells[i+1][j].visited == False:
                directions.append((i+1, j))
            if j > 0 and left and self._cells[i][j-1].visited == False:
                directions.append((i, j-1))
            if j < self._num_cols and right and self._cells[i][j+1].visited == False:
                directions.append((i, j+1))

            if len(directions) == 0:
                break
            ran_dir = random.choice(directions)
            self._cells[i][j].draw_move(self._cells[ran_dir[0]][ran_dir[1]])
            self._draw_cell(i, j)
            solved = self._solve_r(ran_dir[0], ran_dir[1])
            if solved:
                return solved
            self._cells[i][j].draw_move(self._cells[ran_dir[0]][ran_dir[1]], True)
            self._draw_cell(i, j)
        return False

