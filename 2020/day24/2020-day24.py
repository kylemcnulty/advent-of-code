from collections import deque
from itertools import islice
import pprint
import copy

input_filename = "input.txt"
pp = pprint.PrettyPrinter(indent=2)

def part1(instructions):
    tiles = {
        (0,0): 'white'
    }
    for inst in instructions:
        #print("Instruction: {0}".format(inst))
        cur_tile = [0,0] # (q, r)
        i = 0
        while i < len(inst):
            if inst[i:i+1] in ['e', 'w']:
                cmd = inst[i:i+1]
                i += 1
            elif inst[i:i+2] in ['se', 'sw', 'nw', 'ne']:
                cmd = inst[i:i+2]
                i += 2
            
            if cmd == 'e':
                cur_tile[0] += 1 # q
                cur_tile[1] += 0 # r
            elif cmd == 'ne':
                cur_tile[0] += 1 # q
                cur_tile[1] += -1 # r
            elif cmd == 'nw':
                cur_tile[0] += 0 # q
                cur_tile[1] += -1 # r
            elif cmd == 'w':
                cur_tile[0] += -1 # q
                cur_tile[1] += 0 # r
            elif cmd == 'sw':
                cur_tile[0] += -1 # q
                cur_tile[1] += 1 # r                                                            
            elif cmd == 'se':
                cur_tile[0] += 0 # q
                cur_tile[1] += 1 # r

            #print("Moved {0} to tile {1}".format(cmd, cur_tile))

        #print("Navigated to tile: {0}".format(cur_tile))
        cur_tile = tuple(cur_tile)
        if cur_tile in tiles:
            if tiles[cur_tile] is 'white':
                tiles[cur_tile] = 'black'
            elif tiles[cur_tile] is 'black':
                tiles[cur_tile] = 'white'
        else:
            tiles[cur_tile] = 'black'
        #print("Flipped tile to {0}".format(tiles[cur_tile]))
        
    num_black = list(tiles.values()).count('black')
    print("Result: {0}".format(num_black))
    return tiles

def part2(tiles):
    print()

    # Fill in the tiles dictionary with all the mising white tiles
    for q in range(-100,100):
        for r in range(-100,100):
            if (q,r) not in tiles:
                tiles[q,r] = 'white'

    # pp.pprint(tiles)


    for day in range(1, 101):
        # Create copy of the tiles dictionary. We will mark tile changes in this dictionary
        new_tiles = tiles.copy()

        for tile_pos, tile_value in tiles.items():
            # print("\n--- Tile {0} is {1} ---".format(tile_pos, tile_value))
            adjacent_black = check_adjacent_black(tiles, tile_pos)

            # print("It has {0} black neighboring tiles".format(adjacent_black))

            if tile_value == 'black' and (adjacent_black == 0 or adjacent_black > 2):
                # print("---> changing {0} to white".format(tile_pos))
                new_tiles[tile_pos] = 'white'
            elif tile_value == 'white' and adjacent_black == 2:
                new_tiles[tile_pos] = 'black'
                # print("---> changing {0} to black".format(tile_pos))

        num_black = list(new_tiles.values()).count('black')
        print('Day {0}: {1}'.format(day, num_black))
        
        # Now that we've determined new values for tiles, updates 'tiles'
        tiles = new_tiles.copy()

def check_adjacent_black(tiles, tile_pos):
    # Of the 6 tiles immediately adjacent to 'tile', check how many are blac
    neighbors = [(1,0), (1,-1), (0,-1), (-1, 0), (-1, 1), (0, 1)]
    cnt = 0

    for n in neighbors:
        neighbor_tile_pos = (tile_pos[0] + n[0], tile_pos[1] + n[1])
        if neighbor_tile_pos in tiles:
            if tiles[neighbor_tile_pos] == 'black':
                cnt += 1
                # print("neighbor {0} is black".format(neighbor_tile_pos))
            else:
                pass
                # print("neighbor {0} is white".format(neighbor_tile_pos))
        else:
            pass
            # If the adjacent tile isn't listed in our 'tiles' dict, add it
            # print("neighbor {0} dne but is white".format(neighbor_tile_pos))

    return cnt

def main():
    instructions = load_input_file()

    print("\n--- Part 1 ---")
    tiles = part1(instructions)   
    
    print("\n--- Part 2 ---")
    part2(tiles)

def load_input_file():
    instructions= []
    with open(input_filename) as f:
        instructions = f.read().splitlines()
    return instructions

if __name__=="__main__":
    main()