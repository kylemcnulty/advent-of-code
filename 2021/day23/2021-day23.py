input_filename = "input.txt"

def main():
    steps = load_input_file()
    
    #print("\n---Part 1---")
    #part1(steps)
    
    # print("\n---Part 2---")
    # part2(steps)
  
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