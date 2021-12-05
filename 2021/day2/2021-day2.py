input_filename = "input.txt"

def part1(moves):
    pos = 0
    depth = 0
    for m in moves:
        direction, num = m.split(' ')
        num = int(num)        
        if direction == 'forward':
            pos += num
        elif direction == 'down':
            depth += num
        elif direction == 'up':
            depth -= num

    print('Position: {0}, Depth: {1}'.format(pos, depth))
    print('Ans: {0}'.format(pos*depth))

def part2(moves):
    pos = 0
    depth = 0
    aim = 0

    for m in moves:
        direction, num = m.split(' ')
        num = int(num)
        
        if direction == 'forward':
            pos += num
            depth += num * aim
        elif direction == 'down':
            aim += num
        elif direction == 'up':
            aim -= num

    print('Position: {0}, Depth: {1}'.format(pos, depth))
    print('Ans: {0}'.format(pos*depth))
  
def main():
    moves = load_input_file()
    
    print("\n---Part 1---")
    part1(moves)
    
    print("\n---Part 2---")
    part2(moves)
  
def load_input_file():
    moves = []
    with open(input_filename) as f:
        moves = f.read().splitlines()
    return moves

if __name__=="__main__":
    main()