input_filename = "input.txt"

def part1(depths):
    cnt = 1
    for i in range(len(depths)-1):
        if (depths[i] < depths[i + 1]):
            cnt += 1
    print('Ans: {0}'.format(cnt))

def part2(depths):
    cnt = 0
    for i in range(0, len(depths)-3):
        win1_sum = sum(depths[i:i+3])
        win2_sum = sum(depths[i+1:i+4])
        if win1_sum < win2_sum:
            cnt += 1
    print('Ans: {0}'.format(cnt))

def main():
    depths = load_input_file()
    
    print("\n---Part 1---")
    part1(depths)
    
    print("\n--Part 2---")
    part2(depths)
    
def load_input_file():
    depths = []
    with open(input_filename) as f:
        depths = f.read().splitlines()
    depths = list(map(int, depths))
    return depths

if __name__=="__main__":
    main()