input_filename = "input.txt"
import numpy as np

def check_low(height, adjacent_heights):
    adj = adjacent_heights
    if (height < adj[0]) and ((height < adj[1])) and (height < adj[2]) and (height < adj[3]):
        low_point = True
    else:
        low_point = False
    return low_point

def trace_basin(rhm, y, x, basins, basin_size):
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    height = rhm[y, x]
    
    for offset in offsets:
        iy, ix = y + offset[0], x + offset[1]
        adj_height = rhm[iy, ix]
        
        if (adj_height == 9) or (adj_height == 10) or (adj_height < height):
            continue
        elif adj_height > height:    
            if basins[iy, ix] != 1:
                basin_size += 1
                basin_size = trace_basin(rhm, iy, ix, basins, basin_size)
        else:
            continue
    
    basins[y, x] = 1
    return basin_size

def part1(rhm):
    y_max, x_max = rhm.shape
    iy_max, ix_max = y_max-1, x_max-1
    lows = np.zeros((rhm.shape))

    for iy,ix in np.ndindex(rhm.shape):
        height = rhm[iy,ix]
        if (iy == 0) or (iy == iy_max) or (ix == 0) or (ix == ix_max):
            pass
        else:
            adj = [
                rhm[iy-1,ix],
                rhm[iy,ix+1],
                rhm[iy+1,ix],
                rhm[iy,ix-1]
            ]
            if check_low(height, adj):
                lows[iy, ix] = 1

    risk_levels = np.add(np.multiply(lows, rhm), lows)
    ans = int(risk_levels.sum())
    print('Ans: {0}'.format(ans))
    return lows

def part2(rhm, lows):
    y_max, x_max = rhm.shape
    iy_max, ix_max = y_max-1, x_max-1
    
    low_locations = np.nonzero(lows)
    basins = lows.copy()
    basin_sizes = []

    for iy, ix in zip(low_locations[0], low_locations[1]):
        if (iy == 0) or (iy == iy_max) or (ix == 0) or (ix == ix_max):
            pass
        else:
            basin_size = trace_basin(rhm, iy, ix, basins, basin_size=1)
            basin_sizes.append(basin_size)

    largest_basins = sorted(basin_sizes)[-3:]
    ans = np.prod(largest_basins)
    print('Ans: {0}'.format(ans))

def main():
    rhm = load_input_file()
    
    print("\n---Part 1---")
    lows = part1(rhm)
    
    print("\n---Part 2---")
    part2(rhm, lows)
  
def load_input_file():
    lines = []    

    with open(input_filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            line = list(line)
            line = list(map(int, line))
            lines.append(line)

    hm = np.array(lines)
    
    # Ring the heightmap in zeros
    max_height = hm.max()
    rhm = np.full(hm.shape + np.array(2), max_height + 1, hm.dtype)
    rhm[1:-1,1:-1] = hm
    return rhm

if __name__=="__main__":
    main()