from tkinter import Tk, BOTH, Canvas
from line import *
from cell import Cell

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg='white')
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.draw_cell()
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        
    def draw_cell(self):
        pass
#         c1 = Cell(100, 100, 150, 150, self)
#         c1.draw()
#         c2 = Cell(200, 200, 250, 250, self)
#         c2.draw()
# 
#         c1.draw_move(c2, True)
#         
    


