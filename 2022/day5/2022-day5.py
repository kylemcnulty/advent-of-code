import copy
input_filename = "input.txt"

def part1and2(crates, moves, reverse):
    for m in moves:
        num, frm, to = m[0], m[1]-1, m[2]-1
        moving_part = crates[frm][-num:]
        if reverse:
            moving_part.reverse()
        crates[to].extend(moving_part)
        del(crates[frm][-num:])

    ans = ''
    for crate in crates:
        ans += crate[-1]
    return ans

def main():
    crates, moves = load_input_file()
    b = copy.deepcopy(crates)
    c = copy.deepcopy(crates)
    
    ans = part1and2(b, moves, reverse=True)
    print('\nPart 1: {0}'.format(ans))
    
    ans = part1and2(c, moves, reverse=False)
    print('\nPart 2: {0}'.format(ans))
   
def load_input_file():
    lines = []
    with open(input_filename) as f:
        lines = f.read().splitlines()
    
    num_crates = 0
    for line in lines:
        if '[' in line:
            pass
        else:
            a = line.rstrip().lstrip().split('   ')
            num_crates = len(a)
            break

    # create empty list of lists to represent crates
    crates = [ [] for _ in range(num_crates) ]

    moves = []
    for line in lines:
        if '[' in line:
            for c in range(num_crates):
                i = c*4 + 1
                if line[i] != ' ':
                    crates[c].insert(0, line[i])
        elif 'move' in line:
            a = line.split(' ')
            moves.append((int(a[1]), int(a[3]), int(a[5])))
        else:
            pass

    return crates, moves

if __name__=="__main__":
    main()

