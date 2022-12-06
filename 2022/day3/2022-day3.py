input_filename = "input.txt"

def part1(inp):
    total = 0

    for line in inp:
        half_len = len(line)//2
        set1 = set(line[:half_len])
        set2 = set(line[half_len:])
        shared_item = list(set1.intersection(set2))[0]
        
        if shared_item.islower():
            total += ord(shared_item) - 96
        else:
            total += ord(shared_item.lower()) - 96 + 26

    print('\nPart 1: total score is {0}'.format(total))

def part2(inp):
    total = 0
    for i in range(0, len(inp), 3):
        set1, set2, set3 = set(inp[i]), set(inp[i+1]), set(inp[i+2])
        shared_item = list(set1.intersection(set2).intersection(set3))[0]
        
        if shared_item.islower():
            total += ord(shared_item) - 96
        else:
            total += ord(shared_item.lower()) - 96 + 26

    print('\nPart 2: total score is {0}'.format(total))

def main():
    inp = load_input_file()
    part1(inp)
    part2(inp)
    
def load_input_file():
    lines = []
    with open(input_filename) as f:
        lines = f.read().splitlines()
    
    return lines

if __name__=="__main__":
    main()