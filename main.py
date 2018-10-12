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
                break
                
    return clean
    
def search_for_dirty_squares(grid, vacuum_agent, num_rows, num_cols):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param vacuum_agent: Integer tuple
       :param num_rows: Integer
       :param num_cols: Integer'''
    
    num_moves = 0
    while is_grid_clean(grid, num_rows, num_cols) == False and num_moves < 10:
        
        #print("Move #{0}".format(num_moves))
        #print("Vacuum agent is located at square ({0},{1})".format(vacuum_agent[0], vacuum_agent[1]))

        # Check if the square vacuum agent is in is dirty
        dirty_status = grid[vacuum_agent[0]][vacuum_agent[1]].get_dirty_status()
        if dirty_status == True:
            #print("Square ({0},{1}) is dirty.".format(vacuum_agent[0], vacuum_agent[1]))
            grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
            #print("Vacuum agent has cleaned square ({0},{1}).".format(vacuum_agent[0], vacuum_agent[1]))
        else:
            # Find next location to move to
            #print("Square ({0},{1}) is clean.".format(vacuum_agent[0], vacuum_agent[1]))
            next_location = rule_table[vacuum_agent]
            #print("Vacuum agent will move to square ({0},{1})".format(next_location[0], next_location[1]))
            vacuum_agent = next_location
            num_moves += 1
    return num_moves

def main():
    # Grid dimensions
    num_rows = 3
    num_cols = 3

    # Initialize grid
    grid = [[Grid_Square() for j in range(num_cols)] for i in range(num_rows)]
    
    # Randomly assign dirty squares (either 1, 3, or 5) and search
    for num_dirty_squares in [1, 3, 5]:
        # Move stats
        total_moves = 0
        num_moves = 0
        min_moves = 10
        max_moves = 0
        avg_num_moves = 0

        num_iter = 0
        while num_iter < 100:
            # Initialize list of all possible coordinates
            coords = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

            # Initialize list of dirty spot coordinates
            dirty_spots = []

            # Randomly assign coordinates in grid that are dirty
            for i in range(num_dirty_squares):
                rand_index = random.randint(0, (len(coords)-1))
                dirty_spots.append(coords[rand_index])
                coords.remove(coords[rand_index])

            for i in range(num_dirty_squares):
                grid[dirty_spots[i][0]][dirty_spots[i][1]].change_dirt_status(True)

            # Randomly assign vacuum agent to a square
            vacuum_agent = (random.randint(0, 2), random.randint(0, 2))

            # Search for dirty squares
            num_moves = search_for_dirty_squares(grid, vacuum_agent, num_rows, num_cols)
            if num_moves < min_moves:
                min_moves = num_moves
        
            if num_moves > max_moves:
                max_moves = num_moves
        
            total_moves += num_moves
            num_iter += 1

        # Calculate and print out stats
        avg_num_moves = total_moves / 100
        print("\nStats for {0} dirty square(s):".format(num_dirty_squares))
        print("Average number of moves: {0}".format(avg_num_moves))
        print("Max number of moves: {0}".format(max_moves))
        print("Min number of moves: {0}".format(min_moves))
    

if __name__ == '__main__':
    main()

    