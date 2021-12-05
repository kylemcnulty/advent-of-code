from collections import deque
from itertools import islice
import pprint
import copy

input_filename = "input.txt"
pp = pprint.PrettyPrinter(indent=2)

def part1(grid):
    for cycle in range(1, 7):
        grid = pad_grid(grid)
        new_grid = grid.copy()
        for cube_pos, cube_value in grid.items():
            active_neighbors = check_active_neighbors(grid, cube_pos)            
            if cube_value == '#':
                if (active_neighbors == 2 or active_neighbors == 3):
                    pass
                else:
                    new_grid[cube_pos] = '.'
            elif cube_value == '.':
                if active_neighbors == 3:
                    new_grid[cube_pos] = '#'
                else:
                    pass
        
        # Now that we've determined new values for cubes, updates 'cubes'
        grid = new_grid.copy()

    num_active = list(new_grid.values()).count('#')
    print('Result: {0}'.format(num_active))

def pad_grid(grid):
    # Pad the entire grid an extra level of inactive cubes at the start of each round
    x_max = max([key[0] for key in grid.keys()])
    x_min = min([key[0] for key in grid.keys()])
    y_max = max([key[1] for key in grid.keys()])
    y_min = min([key[1] for key in grid.keys()])
    z_max = max([key[2] for key in grid.keys()])
    z_min = min([key[2] for key in grid.keys()])
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                if (x,y,z) not in grid:
                    grid[(x,y,z)] = '.'
    return grid        

def check_active_neighbors(grid, cube_pos):
    # Of the 26 tiles immediately adjacent to 'tile', check how many are blac
    neighbors = [(-1,-1,-1),(-1,-1,0),(-1,-1,1),(-1,0,-1),(-1,0,0),(-1,0,1),(-1,1,-1),(-1,1,0),(-1,1,1),(0,-1,-1),(0,-1,0),(0,-1,1),(0,0,-1),(0,0,1),(0,1,-1),(0,1,0),(0,1,1),(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,-1),(1,0,0),(1,0,1),(1,1,-1),(1,1,0),(1,1,1)]
    cnt = 0

    for n in neighbors:
        neighbor_cube_pos = (cube_pos[0] + n[0], cube_pos[1] + n[1], cube_pos[2] + n[2])
        if neighbor_cube_pos in grid:
            if grid[neighbor_cube_pos] == '#':
                cnt += 1
            else:
                pass
        else:
            # If this neighbor cube isn't in the 'grid' dict, then it is inactive and we don't need it to calculate the total number of active neigbors
            pass
    return cnt

def print_grid(grid, z_slice = None):
    x_max = max([key[0] for key in grid.keys()])
    x_min = min([key[0] for key in grid.keys()])
    y_max = max([key[1] for key in grid.keys()])
    y_min = min([key[1] for key in grid.keys()])
    z_max = max([key[2] for key in grid.keys()])
    z_min = min([key[2] for key in grid.keys()])
    
    for z in range(z_min, z_max + 1):
        if z_slice is not None:
            z = z_slice
        print('\nz = {0}'.format(z))
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                print(grid[(x, y, z)], end="")
            print('')
        if z_slice is not None:
            break

def part2(grid):
    for cycle in range(1, 7):
        grid = pad_grid2(grid)
        new_grid = grid.copy()
        for cube_pos, cube_value in grid.items():
            active_neighbors = check_active_neighbors2(grid, cube_pos)
            if cube_value == '#':
                if (active_neighbors == 2 or active_neighbors == 3):
                    pass
                else:
                    new_grid[cube_pos] = '.'
            elif cube_value == '.':
                if active_neighbors == 3:
                    new_grid[cube_pos] = '#'
                else:
                    pass
        
        # Now that we've determined new values for cubes, updates 'cubes'
        grid = new_grid.copy()

    num_active = list(new_grid.values()).count('#')
    print('Result: {0}'.format(num_active))

def pad_grid2(grid):
    # Pad the entire grid an extra level of inactive cubes at the start of each round
    x_max = max([key[0] for key in grid.keys()])
    x_min = min([key[0] for key in grid.keys()])
    y_max = max([key[1] for key in grid.keys()])
    y_min = min([key[1] for key in grid.keys()])
    z_max = max([key[2] for key in grid.keys()])
    z_min = min([key[2] for key in grid.keys()])
    w_max = max([key[3] for key in grid.keys()])
    w_min = min([key[3] for key in grid.keys()])
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                for w in range(w_min - 1, w_max + 2):
                    if (x,y,z,w) not in grid:
                        grid[(x,y,z,w)] = '.'
    return grid

def check_active_neighbors2(grid, cube_pos):
    # Of the 26 tiles immediately adjacent to 'tile', check how many are blac
    neighbors = [(-1,-1,-1,-1),(-1,-1,-1,0),(-1,-1,-1,1),(-1,-1,0,-1),(-1,-1,0,0),(-1,-1,0,1),(-1,-1,1,-1),(-1,-1,1,0),(-1,-1,1,1),(-1,0,-1,-1),(-1,0,-1,0),(-1,0,-1,1),(-1,0,0,-1),(-1,0,0,0),(-1,0,0,1),(-1,0,1,-1),(-1,0,1,0),(-1,0,1,1),(-1,1,-1,-1),(-1,1,-1,0),(-1,1,-1,1),(-1,1,0,-1),(-1,1,0,0),(-1,1,0,1),(-1,1,1,-1),(-1,1,1,0),(-1,1,1,1),(0,-1,-1,-1),(0,-1,-1,0),(0,-1,-1,1),(0,-1,0,-1),(0,-1,0,0),(0,-1,0,1),(0,-1,1,-1),(0,-1,1,0),(0,-1,1,1),(0,0,-1,-1),(0,0,-1,0),(0,0,-1,1),(0,0,0,-1),(0,0,0,1),(0,0,1,-1),(0,0,1,0),(0,0,1,1),(0,1,-1,-1),(0,1,-1,0),(0,1,-1,1),(0,1,0,-1),(0,1,0,0),(0,1,0,1),(0,1,1,-1),(0,1,1,0),(0,1,1,1),(1,-1,-1,-1),(1,-1,-1,0),(1,-1,-1,1),(1,-1,0,-1),(1,-1,0,0),(1,-1,0,1),(1,-1,1,-1),(1,-1,1,0),(1,-1,1,1),(1,0,-1,-1),(1,0,-1,0),(1,0,-1,1),(1,0,0,-1),(1,0,0,0),(1,0,0,1),(1,0,1,-1),(1,0,1,0),(1,0,1,1),(1,1,-1,-1),(1,1,-1,0),(1,1,-1,1),(1,1,0,-1),(1,1,0,0),(1,1,0,1),(1,1,1,-1),(1,1,1,0),(1,1,1,1)]
    cnt = 0

    for n in neighbors:
        neighbor_cube_pos = (cube_pos[0] + n[0], cube_pos[1] + n[1], cube_pos[2] + n[2], cube_pos[3] + n[3])
        if neighbor_cube_pos in grid:
            if grid[neighbor_cube_pos] == '#':
                cnt += 1
            else:
                pass
        else:
            # If this neighbor cube isn't in the 'grid' dict, then it is inactive and we don't need it to calculate the total number of active neigbors
            pass
    return cnt

def main():
    grid, grid2 = load_input_file()

    print("\n--- Part 1 ---")
    part1(grid)   
    
    print("\n--- Part 2 ---")
    part2(grid2)

def load_input_file():
    grid = {}
    grid2 = {}
    with open(input_filename) as f:
        for y,line in enumerate(f):
            line = line.strip()
            for x,cube in enumerate(line):
                grid[(x, y, 0)] = cube
                grid2[(x, y, 0, 0)] = cube
    
    return grid, grid2

if __name__=="__main__":
    main()