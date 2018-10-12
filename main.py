import random
from grid_square import Grid_Square

def main():
    num_rows = 3
    num_cols = 3

    grid = [[Grid_Square() for j in range(num_cols)] for i in range(num_rows)]

    # Randomly assign a dirty spot in the grid
    dirty_spot = [random.randint(0, 2), random.randint(0, 2)]
    grid[dirty_spot[0]][dirty_spot[1]].change_dirt_status(True)
    print("({0},{1})".format(dirty_spot[0], dirty_spot[1]))
    print(grid[dirty_spot[0]][dirty_spot[1]].print_dirty())


if __name__ == '__main__':
    main()

    