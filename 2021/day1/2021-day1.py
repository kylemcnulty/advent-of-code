# asdf
input_filename = "input.txt"

def part2(depths):
    cnt = 0
    for i in range(2, len(depths)):
        if i == 2:
            win_sum = depths[i] + depths[i-1] + depths[i-2]
            print("{0} N/A".format(win_sum))
        else:
            win1_sum = (depths[i] + depths[i-1] + depths[i-2])
            win2_sum = (depths[i-1] + depths[i-2] + depths[i-3])
            if win1_sum > win2_sum:
                print("{0} (increased)".format(win1_sum))
                cnt += 1
            elif win1_sum == win2_sum:
                print("{0} (no change)".format(win1_sum))
            else:
                print("{0} (decreased)".format(win1_sum))
    print(cnt)

def part1(depths):
    cnt = 1
    for i,d in enumerate(depths):
        if i == 0:
            print("{0} N/A".format(d))
        else:
            if (depths[i] > depths[i - 1]):
                print("{0} (increased)".format(d))
                cnt += 1
            else:
                print("{0} (decreased)".format(d))
    print(cnt)

def main():
    depths = load_input_file()
    
    #print("\n---Part 1---")
    #part1(depths)
    
    print("\n--Part 2---")
    part2(depths)
    
def load_input_file():
    depths = []
    with open(input_filename) as f:
        depths = f.read().splitlines()
    depths = [int(i) for i in depths]
    return depths

if __name__=="__main__":
    main()