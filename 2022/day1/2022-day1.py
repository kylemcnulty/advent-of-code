input_filename = "test_input.txt"

def part1(food):
    print(food)
    cals = []
    for f in food: 
        cals.append(sum(f))
    print(cals)

    cals.sort()
    print(cals)
    max_cal = cals[-1]
  
    print('The elf carrying the most calories is carrying {0} calories'.format(max_cal))

def part2(food):
    cals = []
    for f in food: 
        cals.append(sum(f))
    cals.sort()
    max_three_cals = cals[-3:]
    ans = sum(max_three_cals)

    print('The top-three calorie carrying elves are carrying {0} total calories'.format(ans))

def main():
    food = load_input_file()
    
    print("\n---Part 1---")
    part1(food)
    
    print("\n---Part 2---")
    part2(food)
    
def load_input_file():
    food = []
    elf = []

    with open(input_filename) as f:
        vals = f.read().splitlines()

    for i, v in enumerate(vals):
        if (v == ''):
            food.append(elf)
            elf = []
        else:
            elf.append(int(v))
    food.append(elf)

    return food

if __name__=="__main__":
    main()