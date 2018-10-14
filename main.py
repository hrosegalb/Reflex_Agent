import random
from grid_square import Grid_Square

flag_off_rule_table = {(0,0):(1,0), (0,1):(1,1), (0,2):(0,1), 
              (1,0):(2,0), (1,2):(0,2),
              (2,0):(2,1), (2,1):(2,2), (2,2):(1,2)}

flag_on_rule_table = {(1,1):(0,1), (0,1):(0,0)}


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


def search_for_dirty_squares(grid, num_rows, num_cols):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer'''
    
    # This flag determines which rule table to use
    flag = False
    
    # Randomly assign vacuum agent to a square
    vacuum_agent = (random.randint(0, 2), random.randint(0, 2))
    if vacuum_agent == (1,1):
        flag = True

    num_moves = 0
    while is_grid_clean(grid, num_rows, num_cols) == False and num_moves < 100:

        # Check if the square vacuum agent is in is dirty
        dirty_status = grid[vacuum_agent[0]][vacuum_agent[1]].get_dirty_status()
        if dirty_status == True:
            grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
        else:
            # Find next location to move to
            next_location = tuple()
            if flag == True:
                next_location = flag_on_rule_table[vacuum_agent]
                if next_location == (0,0):
                    flag = False
            else:
                next_location = flag_off_rule_table[vacuum_agent]
                if next_location == (1,1):
                    flag = True

            vacuum_agent = next_location
            num_moves += 1

    return num_moves


def reflex_agent_search(grid, num_rows, num_cols):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer'''

    # Randomly assign dirty squares (either 1, 3, or 5) and search
    for num_dirty_squares in [1, 3, 5]:
        # Move stats
        total_moves = 0
        num_moves = 0
        min_moves = 100
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

            # Search for dirty squares
            num_moves = search_for_dirty_squares(grid, num_rows, num_cols)
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


def random_search_for_dirty_squares(grid, num_rows, num_cols, actions):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer
       :param actions: List of strings'''

    # Randomly assign the vacuum to a spot on the grid
    vacuum_agent = (random.randint(0,2), random.randint(0,2))

    # Begin random search
    num_moves = 0
    while is_grid_clean(grid, num_rows, num_cols) == False and num_moves < 100:
        # Randomly choose an action for the agent
        rand_index = random.randint(0, (len(actions)-1))

        # Perform action
        if actions[rand_index] == "suck":
            grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
        elif actions[rand_index] == "nothing":
            pass
        else:
            next_location = tuple()
            if actions[rand_index] == "left":
                next_location = (vacuum_agent[0], vacuum_agent[1]-1)
            elif actions[rand_index] == "right":
                next_location = (vacuum_agent[0], vacuum_agent[1]+1)
            elif actions[rand_index] == "up":
                next_location = (vacuum_agent[0]-1, vacuum_agent[1])
            else:
                next_location = (vacuum_agent[0]+1, vacuum_agent[1])
        
            if next_location[0] < 0 or next_location[0] > 2 or next_location[1] < 0 or next_location[1] > 2:
                next_location = vacuum_agent
            vacuum_agent = next_location

            num_moves += 1

    return num_moves


def randomized_agent_search(grid, num_rows, num_cols, actions):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer
       :param actions: List of strings'''
    
        # Randomly assign dirty squares (either 1, 3, or 5) and search
    for num_dirty_squares in [1, 3, 5]:
        # Move stats
        total_moves = 0
        num_moves = 0
        min_moves = 100
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

            # Search for dirty squares
            num_moves = random_search_for_dirty_squares(grid, num_rows, num_cols, actions)
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

def reflex_agent_search_dirty_squares_murphys_law(grid, num_rows, num_cols):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer'''

    # This flag determines which rule table to use
    flag = False

    # Randomly assign vacuum agent to a square
    vacuum_agent = (random.randint(0, 2), random.randint(0, 2))
    if vacuum_agent == (1,1):
        flag = True

    num_moves = 0
    murphys_law_counter = 0
    dirt_sensor_counter = 0
    while is_grid_clean(grid, num_rows, num_cols) == False and num_moves < 100:
        # Check if the square vacuum agent is in is dirty
        dirty_status = grid[vacuum_agent[0]][vacuum_agent[1]].get_dirty_status()

        if murphys_law_counter % 4 == 0 and dirt_sensor_counter % 10 == 0:
            # There are two scenarios that can happen here:
            # (1) Floor is dirty, but sensor thinks it's clean; agent deposits more dirt.  
            # (2) Floor is clean, but sensor thinks it's dirty; suck action fails to clean floor,
            # but it doesn't matter because floor is already clean.
            pass
        elif murphys_law_counter % 4 == 0:
            # Either floor is dirty and suck action fails to work or floor is clean and agent deposits
            # more dirt onto the floor
            grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(True)

            # Agent moves to next location.
            next_location = tuple()
            if flag == True:
                next_location = flag_on_rule_table[vacuum_agent]
                if next_location == (0,0):
                    flag = False
            else:
                next_location = flag_off_rule_table[vacuum_agent]
                if next_location == (1,1):
                    flag = True
            vacuum_agent = next_location
            num_moves += 1         
        elif dirt_sensor_counter % 10 == 0:
            if dirty_status == True:
                # Sensor will think floor is clean, so it chooses next move
                next_location = tuple()
                if flag == True:
                    next_location = flag_on_rule_table[vacuum_agent]
                    if next_location == (0,0):
                        flag = False
                else:
                    next_location = flag_off_rule_table[vacuum_agent]
                    if next_location == (1,1):
                        flag = True
                vacuum_agent = next_location
                num_moves += 1
            else:
                # Sensor thinks floor is dirty, so it chooses to suck
                grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
        else:
            # Murphy's Law not in effect
            if dirty_status == True:
                grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
            else:
                # Find next location to move to
                next_location = tuple()
                if flag == True:
                    next_location = flag_on_rule_table[vacuum_agent]
                    if next_location == (0,0):
                        flag = False
                else:
                    next_location = flag_off_rule_table[vacuum_agent]
                    if next_location == (1,1):
                        flag = True
                vacuum_agent = next_location
                num_moves += 1

        murphys_law_counter += 1
        dirt_sensor_counter += 1

    return num_moves

def reflex_agent_search_murphys_law(grid, num_rows, num_cols):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer'''

    # Randomly assign dirty squares (either 1, 3, or 5) and search
    for num_dirty_squares in [1, 3, 5]:
        # Move stats
        total_moves = 0
        num_moves = 0
        min_moves = 100
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

            # Search for dirty squares
            num_moves = reflex_agent_search_dirty_squares_murphys_law(grid, num_rows, num_cols)
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

def randomized_agent_search_dirty_squares_murphys_law(grid, num_rows, num_cols, actions):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer
       :param actions: List of Strings'''

    # Randomly assign the vacuum to a spot on the grid
    vacuum_agent = (random.randint(0,2), random.randint(0,2))
    #print("Vacuum agent has been assigned spot {0}".format(vacuum_agent))

    # Begin random search
    murphys_law_counter = 0
    num_moves = 0
    while is_grid_clean(grid, num_rows, num_cols) == False and num_moves < 100:
        # Randomly choose an action for the agent
        rand_index = random.randint(0, (len(actions)-1))
        #print("Agent is now at {0}. Action chosen is {1}.".format(vacuum_agent, actions[rand_index]))

        # Perform action
        if actions[rand_index] == "suck":
            if murphys_law_counter % 4 == 0:
                grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(True)
                #print("Murphy's Law in effect. Spot remains dirty or has been made dirty.")
            else:
                grid[vacuum_agent[0]][vacuum_agent[1]].change_dirt_status(False)
            murphys_law_counter += 1
        elif actions[rand_index] == "nothing":
            pass
        else:
            next_location = tuple()
            if actions[rand_index] == "left":
                next_location = (vacuum_agent[0], vacuum_agent[1]-1)
            elif actions[rand_index] == "right":
                next_location = (vacuum_agent[0], vacuum_agent[1]+1)
            elif actions[rand_index] == "up":
                next_location = (vacuum_agent[0]-1, vacuum_agent[1])
            else:
                next_location = (vacuum_agent[0]+1, vacuum_agent[1])
        
            if next_location[0] < 0 or next_location[0] > 2 or next_location[1] < 0 or next_location[1] > 2:
                next_location = vacuum_agent
            vacuum_agent = next_location

            num_moves += 1

    return num_moves

def randomized_agent_search_murphys_law(grid, num_rows, num_cols, actions):
    ''':param grid: 3 x 3 matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer
       :param actions: List of Strings'''

    # Randomly assign dirty squares (either 1, 3, or 5) and search
    for num_dirty_squares in [1, 3, 5]:
        # Move stats
        total_moves = 0
        num_moves = 0
        min_moves = 100
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

            # Search for dirty squares
            num_moves = randomized_agent_search_dirty_squares_murphys_law(grid, num_rows, num_cols, actions)
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

def clean_up_grid(grid, num_rows, num_cols):
    ''':param grid: 3 x 3 Matrix of Grid_Squares
       :param num_rows: Integer
       :param num_cols: Integer'''

    for i in range(num_rows):
        for j in range(num_cols):
            grid[i][j].change_dirt_status(False)

    

def main():
    # List of actions the agent could choose
    actions = ["left", "right", "up", "down", "suck", "nothing"]

    # Grid dimensions
    num_rows = 3
    num_cols = 3

    # Initialize grid
    grid = [[Grid_Square() for j in range(num_cols)] for i in range(num_rows)]

    # Do part (i) of homework - reflex agent search
    print("\n(i) Reflex agent")
    reflex_agent_search(grid, num_rows, num_cols)

    clean_up_grid(grid, num_rows, num_cols)

    # Do part (ii) of homework - randomized agent search
    print("\n(ii) Random agent")
    randomized_agent_search(grid, num_rows, num_cols, actions)

    clean_up_grid(grid, num_rows, num_cols)

    # Do part (iii) of homework - reflex agent search w/ Murphy's Law
    # 25% of time suck action fails to clean floor if it's dirty/deposits dirt if it's clean
    # 10% of time dirt sensor fails and gives wrong answer
    print("\n(iii) Reflex agent w/ Murphy's Law")
    reflex_agent_search_murphys_law(grid, num_rows, num_cols)

    clean_up_grid(grid, num_rows, num_cols)

    # Do part (iv) of homework - randomized agent search w/ Murphy's Law
    # 25% of time suck action fails to clean floor if it's dirty/deposits dirt if it's clean
    # 10% of time dirt sensor fails and gives wrong answer
    print("\n(iv) Random agent w/ Murphy's Law")
    randomized_agent_search_murphys_law(grid, num_rows, num_cols, actions)








    

if __name__ == '__main__':
    main()

    