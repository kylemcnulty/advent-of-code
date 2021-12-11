input_filename = "input.txt"
import numpy as np

def get_neighbors(rgrid, y, x):
    ''' Returns indices of all neighboring elements, including diagonals'''
    y_max, x_max = rgrid.shape
    iy_max, ix_max = y_max-1, x_max-1
    neighbors = []
    offsets = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    for offset in offsets:
        iy, ix = y + offset[0], x + offset[1]
        
        if (iy < 0) or (iy > iy_max) or (ix < 0) or (ix > ix_max):
            continue
        else:
            neighbors.append((iy,ix))
    return neighbors

def flash(rgrid, y, x):
    # Set this flashing octopus to -1 to denote that it has just flashed
    rgrid[y,x] = -1
    
    # Increase the energy level of all neighbors by 1
    neighbors = get_neighbors(rgrid, y, x)
    for niy,nix in neighbors:
        if rgrid[niy,nix] == -1:
            # then ignore because this octopus has already flashed during this step
            continue
        else:
            rgrid[niy,nix] += 1
    
    # Check for all flashing octopuses and iterate through each of them, propagating their flashes
    flashing = np.where(rgrid > 9)
    for iy,ix in zip(flashing[0], flashing[1]):
        if rgrid[iy,ix] == -1:
            # then ignore because this octopus has already flashed during this step
            continue
        else:
            flash(rgrid, iy, ix)
    return

def part12(rgrid, steps):
    num_flashes = 0
    part1_ans = None
    part2_ans = None
    step = 1

    while True:
        # First, increase the energy level of all octopuses by 1
        rgrid += 1

        # Start the flash propagation (recursion) with the first flashing octopus in the grid
        flashing = np.where(rgrid > 9)
        if flashing[0].size != 0:
            first_flash = list(zip(flashing[0], flashing[1]))[0]
            flash(rgrid, first_flash[0], first_flash[1])

        # Count the number of octopuses that flashed during this step. Flashing octopus are marked by an 
        # energy level of -1.
        num_flashed = np.count_nonzero(rgrid == -1)
        num_flashes += num_flashed
        if num_flashed == rgrid.size:
            part2_ans = step

        if step == steps:
            part1_ans = num_flashes        

        # For every octopus that flashed during this step, set their energy level to 0.
        rgrid[rgrid == -1] = 0

        # If we have an answer to part 2 and we have run enough steps for part 1, break out of the loop
        if (part2_ans is not None) and (step > steps):
            break

        step += 1

    print('Ans: {0} flashes after {1} steps'.format(part1_ans, steps))
    print("Ans: Every octopus flashed simultaneously on step {0}".format(part2_ans))

def main():
    rgrid = load_input_file()
    
    print("\n---Part 1 and 2---")
    part12(rgrid, steps=100)
    
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

    rgrid = np.array(lines)
    return rgrid

if __name__=="__main__":
    main()