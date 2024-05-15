from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(100, 50, num_rows, num_cols, 50, 50, win, seed=0)
    m1.solve()
    win.wait_for_close()





if __name__ == "__main__":
    main()

