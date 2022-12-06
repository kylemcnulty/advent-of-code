input_filename = "input.txt"

def part1(inp):
    cnt_secs = 0
    for a in inp:
        #print(a)
        if a[0] >= a[2] and a[1] <= a[3]:
            # first section is fully contained in second section
            cnt_secs += 1
        elif a[2] >= a[0] and a[3] <= a[1]:
            # second section is fully contained in first section
            cnt_secs += 1 
        else:
            pass

    print('\nPart 1: there are {0} fully overlapping assignment pairs'.format(cnt_secs))

def part2(inp):
    cnt_secs = 0
    for a in inp:
        set1 = set(range(a[0], a[1]+1))
        set2 = set(range(a[2], a[3]+1))
        overlap = set1.intersection(set2)
        if len(overlap) != 0:
            cnt_secs += 1

    print('\nPart 2: there are {0} partially overlapping assignment pairs'.format(cnt_secs))

def main():
    inp = load_input_file()
    part1(inp)
    part2(inp)
   
def load_input_file():
    lines = []
    with open(input_filename) as f:
        lines = f.read().splitlines()
    
    for i,line in enumerate(lines):
        a = line.split(',')
        b = (
                int(a[0].split('-')[0]), 
                int(a[0].split('-')[1]),
                int(a[1].split('-')[0]),
                int(a[1].split('-')[1]),
            )
        lines[i] = b
    return lines

if __name__=="__main__":
    main()

