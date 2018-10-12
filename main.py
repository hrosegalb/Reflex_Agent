import random
from grid_square import Grid_Square

rule_table = {(0,0):(1,0), (0,1):(1,1), (0,2):(0,1), 
              (1,0):(2,0), (1,1):(0,0), (1,2):(0,2),
              (2,0):(2,1), (2,1):(2,2), (2,2):(1,2)}

def is_grid_clean(grid, num_rows, num_cols):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer'''

    clean = True
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j].get_dirty_status() == True:
                clean = False
                
    return clean
    

def main():
    num_rows = 3
    num_cols = 3

    grid = [[Grid_Square() for j in range(num_cols)] for i in range(num_rows)]

    # Randomly assign a dirty spot in the grid
    dirty_spot = [random.randint(0, 2), random.randint(0, 2)]
    grid[dirty_spot[0]][dirty_spot[1]].change_dirt_status(True)
    
    #print("({0},{1})".format(dirty_spot[0], dirty_spot[1]))
    #print(grid[dirty_spot[0]][dirty_spot[1]].print_dirty())

    print("Dirty square is located at ({0},{1})".format(dirty_spot[0], dirty_spot[1]))

    # Randomly assign vacuum agent to a square
    vacuum_agent = (random.randint(0, 2), random.randint(0, 2))

    # Search for dirty squares
    num_moves = 0
    while is_grid_clean(grid, num_rows, num_cols) == False and num_moves < 10:
        
        print("Move #{0}".format(num_moves))
        print("Vacuum agent is located at square ({0},{1})".format(vacuum_agent[0], vacuum_agent[1]))

        # Check if the square vacuum agent is in is dirty
        dirty_status = grid[vacuum_agent[0]][vacuum_agent[1]].get_dirty_status()
        if dirty_status == True:
            print("Square ({0},{1}) is dirty.".format(vacuum_agent[0], vacuum_agent[1]))
            grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
            print("Vacuum agent has cleaned square ({0},{1}).".format(vacuum_agent[0], vacuum_agent[1]))
        else:
            # Find next location to move to
            print("Square ({0},{1}) is clean.".format(vacuum_agent[0], vacuum_agent[1]))
            next_location = rule_table[vacuum_agent]
            print("Vacuum agent will move to square ({0},{1})".format(next_location[0], next_location[1]))
            vacuum_agent = next_location
            num_moves += 1

    clean_status = is_grid_clean(grid, num_rows, num_cols)
    print("Grid is clean: {0}".format(clean_status))
    print("Total number of moves: {0}".format(num_moves))
    




if __name__ == '__main__':
    main()

    