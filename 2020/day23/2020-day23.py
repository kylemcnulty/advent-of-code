from collections import deque
from itertools import islice
import pprint
import copy

def part1(cups):
    num_cups = len(cups)
    cups = play(cups, moves=100)
    result = ''
    idx1 = cups.index(1)
    for cnt in range(1,num_cups):
        cnt = (idx1 + cnt) % num_cups
        result += str(cups[cnt])

    print("Result: {0}".format(result))

def part2(cups):
    max_cup = max(cups)
    more_cups = list(range(max_cup + 1, 1000000 + 1))
    cups = cups + more_cups
    num_cups = len(cups)

    cups = play(cups, moves=10000000)
   
    idx1 = cups.index(1) # get the index of cup 1
    val1 = cups[idx1 + 1]
    val2 = cups[idx1 + 2]
    result = val1 * val2

    print("Result: {0}".format(result))

def play(cups, moves):
    # for cups list, clockwise = right, ccw = left
    cups = deque(cups)
    num_cups = len(cups)
    lowest_cup = min(cups)

    for move in range(0, moves):
        # print('\n-- move {0} --'.format(move+1))
        if (move % 1000) == 0:
            print("reached move {0}".format(move))

        cur_cup_idx = move % num_cups
        cur_cup = cups[cur_cup_idx]
        # print('cups: {0}'.format(cups))
        # print('current cup: {0}'.format(cur_cup))
        
        # The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        pickup = [None] * 3
        pickup[0] = cups[((cur_cup_idx + 1) % (num_cups))]
        pickup[1] = cups[((cur_cup_idx + 2) % (num_cups))]
        pickup[2] = cups[((cur_cup_idx + 3) % (num_cups))]
        cups.remove(pickup[0])
        cups.remove(pickup[1])
        cups.remove(pickup[2])
        # print('pick up: {0}'.format(pickup))

        # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
        dest_cup = cur_cup - 1
        while dest_cup in pickup:
            dest_cup -= 1
        if dest_cup < lowest_cup:
            dest_cup = max(cups)
        dest_cup_idx = cups.index(dest_cup)
        # print("destination: {0} w/ index {1}".format(dest_cup, dest_cup_idx))

        # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
        cups.insert(((dest_cup_idx + 1) % num_cups), pickup[0])
        cups.insert(((dest_cup_idx + 2) % num_cups), pickup[1])
        cups.insert(((dest_cup_idx + 3) % num_cups), pickup[2])

        # Shift the buffer to the current cup is in the right index (cur_cup_idx)
        cur_cup_shifted_idx = cups.index(cur_cup)
        n = cur_cup_idx - cur_cup_shifted_idx
        cups.rotate(n)
        #cups = cups[-n:] + cups[:-n]

    print("\n-- final --")
    print('cups: {0}'.format(cups))
    return cups

def main():
    test_input = '389125467'
    puzzle_input = '952316487'
    cups = list(puzzle_input)
    cups = [int(c) for c in cups]

    print("\n--- Part 1 ---")
    part1(cups)

    #print("\n--- Part 2 ---")
    #part2(cups)

if __name__=="__main__":
    main()