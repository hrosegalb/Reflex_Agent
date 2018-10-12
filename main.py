import numpy as np
from grid_square import Grid_Square

def main():
    num_rows = 3
    num_cols = 3

    grid = [[Grid_Square() for i in range(3)], [Grid_Square() for i in range(3)], [Grid_Square() for i in range(3)]]

    for i in range(num_rows):
        for j in range(num_cols):
            print("{0},{1}".format(i, j))
            print(grid[i][j].print_dirty())

if __name__ == '__main__':
    main()

    