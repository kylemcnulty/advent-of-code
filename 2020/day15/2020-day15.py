def part1(starting_nums, turns):
    spoken = {} # will be list of dicts
    last_num = None

    for turn in range(1, turns+1):
        if (turn-1) < len(starting_nums):
            # Then use a starting number for this turn
            cur_num = starting_nums[turn-1]
            spoken[cur_num] = []
            spoken[cur_num].append(turn)
        else:
            if len(spoken[last_num]) == 1:
                # Last number spoken was spoken for the first time
                cur_num = 0
            else:
                last_age = spoken[last_num][-1] - spoken[last_num][-2]
                cur_num = last_age

        # Speak the current number 
        if cur_num in spoken:
            spoken[cur_num].append(turn)
        else:
            spoken[cur_num] = []
            spoken[cur_num].append(turn)
        last_num = cur_num

        if turn % 300000 == 0:
            # Print status indicator to terminal
            print("Reached turn {0}".format(turn))

    print(cur_num)
    return

def main():
    test_1 = [0, 3, 6]
    actual_input = [1,2,16,19,18,0]
    numbers = actual_input
 
    print("\n---Part 1---")
    part1(numbers, 2020)

    print("\n---Part 2---")
    part1(numbers, 30000000)
 
if __name__=="__main__":
    main()