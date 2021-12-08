import statistics as stat
input_filename = "input.txt"

def part1(crabs):
    best_pos = stat.median(crabs)
    fuel = 0
    for crab in crabs:
        fuel += int(abs(crab - best_pos))

    print('Ans: The best position is {0} w/ fuel consumption: {1}'.format(best_pos, fuel))

def part2(crabs):
    max_pos = max(crabs)
    
    positions = {} # key is position; value is fuel requirement
    for pos in range(0, max_pos):
        fuel = 0
        for crab_pos in crabs:
            diff = abs(crab_pos - pos)
            fuel += int((diff*diff + diff) / 2)
        positions[pos] = fuel

    min_fuel = min(positions.values())
    best_pos = None
    for pos,fuel in positions.items():
        if fuel == min_fuel:
            best_pos = pos
            break

    print("Ans: The best position is {0} w/ fuel consumption: {1}".format(best_pos, min_fuel))

def main():
    crabs = load_input_file()
    
    print("\n---Part 1---")
    part1(crabs)
    
    print("\n---Part 2---")
    part2(crabs)
  
def load_input_file():
    crabs = []
    
    with open(input_filename) as f:
        line = f.readline().strip()
        crabs = line.split(',')
        crabs = list(map(int, crabs))
    return crabs

if __name__=="__main__":
    main()