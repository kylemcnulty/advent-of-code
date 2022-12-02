input_filename = "input.txt"
import numpy as np
import pprint
import itertools
from collections import defaultdict

def count_on(grid):
    cnt = 0
    sl = 50
    for cube,state in grid.items():
        if (-sl <= cube[0] <= sl) and (-sl <= cube[1] <= sl) and (-sl <= cube[2] <= sl):
            if state == True:
                cnt += 1
    return cnt

def def_value():
    return 0

def part1(steps):
    grid = defaultdict(def_value)

    for step in steps:
        print('Processing {0}'.format(step))
        state, cuboid = step['state'], step['cuboid']
        xran = range(cuboid[0][0], cuboid[0][1]+1)
        yran = range(cuboid[1][0], cuboid[1][1]+1)
        zran = range(cuboid[2][0], cuboid[2][1]+1)
        cubes = list(itertools.product(xran, yran, zran))

        for c in cubes:
            if state == 'on':
                grid[c] = True
            elif state == 'off':
                grid[c] = False

        on_cnt = count_on(grid)
        print('{0} cubes turned on'.format(on_cnt))
        
    on_cnt = count_on(grid)
    print('{0} cubes turned on'.format(on_cnt))

def part2(steps):
    grid = defaultdict(def_value)

    on_cnt = 0

    for i,step in enumerate(steps):
        print('Processing {0}'.format(step))
        istate, icuboid = step['state'], step['cuboid']

        ran = [
            range(icuboid[0][0], icuboid[0][1]+1),
            range(icuboid[1][0], icuboid[1][1]+1),
            range(icuboid[2][0], icuboid[2][1]+1),
        ]
        cnt = [
            icuboid[0][1] - icuboid[0][0],
            icuboid[1][1] - icuboid[1][0],
            icuboid[2][1] - icuboid[2][0],
        ]
        cubes = list(itertools.product(ran[0], ran[1], ran[2]))
        num_cubes = cnt[0] * cnt[1] * cnt[2]

        if (i == 0) and (istate == 'on'):
            on_cnt += num_cubes



        
        
        # for j in range(0,i):
            # jstate, jcuboid = step['state'], step['cuboid']

            # if j



        # print('{0} x {1} x {2} cube'.format(xs, ys, zs))
        print(num_cubes)
        print(on_cnt)
        input()

        # for c in cubes:
        #     if state == 'on':
        #         grid[c] = 1
        #     elif state == 'off':
        #         grid[c] = 0
        
    # on_cnt = count_on(grid)
    # print('{0} cubes turned on'.format(on_cnt))

def main():
    steps = load_input_file()
    
    #print("\n---Part 1---")
    #part1(steps)
    
    print("\n---Part 2---")
    part2(steps)
  
def load_input_file():
    steps = []
    with open(input_filename) as f:
        for line in f.readlines():
            line = line.strip()
            state, dims = line.split(' ')
            dims = dims.split(',')
            cuboid = []
            for dim in dims:
                d = dim.split('=')[1].split('..')
                d = tuple(map(int, d))
                cuboid.append(d)                

            steps.append(
                {
                    'state': state,
                    'cuboid': cuboid 
                }
            )
    
    # pprint.pprint(steps)
    return steps

if __name__=="__main__":
    main()