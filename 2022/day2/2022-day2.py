input_filename = "input.txt"



def part1(strat):
    # A, X = rock
    # B, Y = paper
    # C, Z = scissors
    # z beats b
    # y beats a
    # x beats c
    score = 0
    score_map = {'X': 1, 'Y': 2, 'Z': 3}

    for r in strat:
        shape_score = score_map[r[1]]
        if r in [['A', 'X'], ['B', 'Y'], ['C', 'Z']]:
            score += (shape_score + 3)
        elif r[0] == 'C' and r[1] == 'X':
            score += (shape_score + 6)
        elif r[0] == 'A' and r[1] == 'Y':
            score += (shape_score + 6)
        elif r[0] == 'B' and r[1] == 'Z':
            score += (shape_score + 6)
        else:
            score += (shape_score + 0)

    print('\nPart 1: your total score is {0}'.format(score))

def part2(strat):
    # X = you lose
    # Y = you draw
    # Z = you win
    score = 0
    score_map = {'X': 1, 'Y': 2, 'Z': 3}

    for r in strat:
        if r[1] == 'Y' and r[0] == 'A':
            score += score_map['X'] + 3
        elif r[1] == 'Y' and r[0] == 'B':
            score += score_map['Y'] + 3
        elif r[1] == 'Y' and r[0] == 'C':
            score += score_map['Z'] + 3
    
        elif r[1] == 'X' and r[0] == 'A':
            score += score_map['Z']
        elif r[1] == 'X' and r[0] == 'B':
            score += score_map['X']
        elif r[1] == 'X' and r[0] == 'C':
            score += score_map['Y']
        
        elif r[1] == 'Z' and r[0] == 'A':
            score += score_map['Y'] + 6
        elif r[1] == 'Z' and r[0] == 'B':
            score += score_map['Z'] + 6
        elif r[1] == 'Z' and r[0] == 'C':
            score += score_map['X'] + 6

    print('\nPart 2: your total score is {0}'.format(score))

def main():
    strat = load_input_file()
    part1(strat)
    part2(strat)
    
def load_input_file():
    strat = []
    with open(input_filename) as f:
        strat = f.read().splitlines()

    for i,r in enumerate(strat):
        strat[i] = r.split(' ')

    return strat

if __name__=="__main__":
    main()