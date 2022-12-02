import pprint
input_filename = "input.txt"
from itertools import combinations

def part1(program):
    lowest =     # 10,000,000,000,000
    highest = (10*lowest) - 1
    
    for num in range(highest, lowest, -1):
        snum = str(num)
        if '0' not in snum:
            valid = check_number(snum, program)

            if valid:
                print('Number: {0} is valid'.format(num))
                break
            else:
                continue

        # Status checker
        if num % 1000000 == 0:
            print('Reached number: {0}'.format(num))

    print('Number: {0} is {1}'.format(num, valid))

def check_number(number, program):
    ivars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    num_inps = 0
    for line in program:
        # print('\nLine: {0}'.format(line))

        op, arg1, arg2 = line
        if arg2 in ['w', 'x', 'y', 'z']:
            arg2 = ivars[arg2]
        else:
            arg2 = arg2

        if op == 'inp':
            ivars[arg1] = int(number[num_inps])
            num_inps += 1
        elif op == 'add':
            ivars[arg1] = ivars[arg1] + arg2
        elif op == 'mul':
            ivars[arg1] = ivars[arg1] * arg2
        elif op == 'div':
            ivars[arg1] = int(ivars[arg1] / arg2)
        elif op == 'mod':
            ivars[arg1] = ivars[arg1] % arg2
        elif op == 'eql':
            if ivars[arg1] == arg2:
                ivars[arg1] = 1
            else:
                ivars[arg1] = 0

    # print('\nFinal')
    # pprint.pprint(ivars)
    if ivars['z'] == 0:
        # print("Number was valid")
        return True
    else:
        # print('Number was not valid')
        return False

def main():
    program = load_input_file()
    
    print("\n---Part 1---")
    part1(program)
    
def load_input_file():
    program = []

    with open(input_filename) as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            if len(line) > 2:
                try:
                    line[2] = int(line[2])
                except ValueError:
                    pass
            else:
                line.append(None)
            program.append(line)

    return program

if __name__=="__main__":
    main()