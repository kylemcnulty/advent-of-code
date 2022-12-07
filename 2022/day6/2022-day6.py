input_filename = "input.txt"

def part1and2(subr, num_unique):
    marker_pos = None
    for i in range(num_unique, len(subr)+1):
        a = subr[i-num_unique:i]

        if len(set(a)) == num_unique:
            marker_pos = i
            break
    return marker_pos

def main():
    subr = load_input_file()
    
    ans = part1and2(subr, num_unique=4)
    print('Part 1: the marker is found at character {0}'.format(ans))
    
    ans = part1and2(subr, num_unique=14)
    print('Part 2: the marker is found at character {0}'.format(ans))
   
def load_input_file():
    subr = ''
    with open(input_filename) as f:
        subr = f.readline().rstrip()
    return subr

if __name__=="__main__":
    main()

