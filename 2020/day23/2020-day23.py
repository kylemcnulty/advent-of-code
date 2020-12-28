from collections import deque
from itertools import islice
import pprint
import copy

debug = False

def part1(cups):
    current_cup = cups[0]
    cups = create_cups_dict(cups)
    cups = play2(cups, current_cup, moves=100)
    result = ''
    cup = cups[1]
    while True:
        result += str(cup)
        cup = cups[cup]
        if cup == 1:
            break

    print("Result: {0}".format(result))

def part2(cups):
    current_cup = cups[0]
    max_cup = max(cups)
    more_cups = list(range(max_cup + 1, 1000000 + 1))
    cups = cups + more_cups
    cups = create_cups_dict(cups)
    cups = play2(cups, current_cup, moves=10000000)
   
    val1 = cups[1]
    val2 = cups[cups[1]]
    result = val1 * val2

    print("Result: {0}".format(result))

def create_cups_dict(cups):
    # Convert the 'cups' list to a dictionary that represents a singly linked list. The keys are cup labels and values are the label of the subsequent cup. For example, consider list [1, 9, 2, 4]. The cups dict would be: {1: 9, 9: 2, 2: 4, 4: 1}. This allows for easy forward traversal of the cups. With this implementation, you cannot efficiently traverse backwards.
    num_cups = len(cups)
    current_cup = cups[0]
    cups_dict = {}
    for i in range(0, num_cups):
        if i < (num_cups - 1):
            cups_dict[cups[i]] = cups[i+1]
        else:
            cups_dict[cups[i]] = cups[0]
    return cups_dict

def play(cups, moves):
    debug_interval = 10000
    # for cups list, clockwise = right, ccw = left
    num_cups = len(cups)
    cups = deque(cups, maxlen=num_cups)
    lowest_cup = min(cups)
    max_cup = max(cups)
    cur_cup_idx = 0

    for move in range(0, moves):
        if (move % debug_interval) == 0:
            print("\n -- Move {0} --".format(move + 1))

        cur_cup = cups[cur_cup_idx]
        if (move % debug_interval) == 0:
            print_cups(cups, cur_cup)
    
        if (move % debug_interval) == 0:
            print("current: {0} w/ index {1}".format(cur_cup, cur_cup_idx))
    
        # The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        pickup = [None] * 3
        pickup[0] = cups[((cur_cup_idx + 1) % (num_cups))]
        pickup[1] = cups[((cur_cup_idx + 2) % (num_cups))]
        pickup[2] = cups[((cur_cup_idx + 3) % (num_cups))]
        cups.remove(pickup[0])
        cups.remove(pickup[1])
        cups.remove(pickup[2])
        if (move % debug_interval) == 0:
            print('pick up: {0}'.format(pickup))

        # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
        dest_cup = cur_cup - 1
        while dest_cup in pickup:
            dest_cup -= 1
        if dest_cup < lowest_cup:
            dest_cup = max_cup
            while dest_cup in pickup:
                dest_cup -= 1
        
        dest_cup_idx = cups.index(dest_cup)
        
        if (move % debug_interval) == 0:
            print("destination: {0} w/ index {1}".format(dest_cup, dest_cup_idx))
            print_cups(cups, cur_cup, dest_cup)

        # Calculate the clockwise distance between the current cup and destination cup
        distance = dest_cup_idx - cur_cup_idx
        # if cw_distance < 0:
        #     cw_distance = num_cups + cw_distance
        if (move % debug_interval) == 0:
            print("Distance from current cup --> dest cup: {0}".format(distance))

        # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
        cups.insert(((dest_cup_idx + 1) % num_cups), pickup[0])
        cups.insert(((dest_cup_idx + 2) % num_cups), pickup[1])
        cups.insert(((dest_cup_idx + 3) % num_cups), pickup[2])

        # Shift the buffer to the current cup is in the right index (cur_cup_idx)        
        if ((cur_cup_idx - 4) >= 0) and ((cur_cup_idx + 4) < num_cups):
            start = cur_cup_idx - 4
            stop = (cur_cup_idx + 4)
            cur_cup_shifted_idx = cups.index(cur_cup, start, stop)
        else:
            cur_cup_shifted_idx = cups.index(cur_cup)
        n = cur_cup_idx - cur_cup_shifted_idx
        cups.rotate(n)

        if (move % debug_interval) == 0:
            print_cups(cups, cur_cup, dest_cup)
            # input()

        # Update the cur_cup_idx
        cur_cup_idx += 1
        if cur_cup_idx >= num_cups:
            cur_cup_idx = 0 

    print("\n-- final --")
    # print('cups: {0}'.format(cups))
    return cups

def play2(cups, current_cup, moves):
    global debug
    debug_interval = 1000000
    num_cups = len(cups)
    lowest_cup = min(cups.keys())
    max_cup = max(cups.keys())

    for move in range(0, moves):
        if debug and (move % debug_interval) == 0:
            print("\n -- Move {0} --".format(move + 1))
            print_cups2(cups, current_cup)
    
        # The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        pickup = [None] * 3
        pickup[0] = cups[current_cup]
        pickup[1] = cups[ cups[current_cup] ]
        pickup[2] = cups[ cups[ cups[current_cup] ] ]
        cups[current_cup] = cups[ cups[ cups[ cups[current_cup] ] ] ]
        if debug and (move % debug_interval) == 0:
            print('pick up: {0}'.format(pickup))
            print_cups2(cups, current_cup)

        # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
        dest_cup = current_cup - 1
        while dest_cup in pickup:
            dest_cup -= 1
        if dest_cup < lowest_cup:
            dest_cup = max_cup
            while dest_cup in pickup:
                dest_cup -= 1

        if debug and (move % debug_interval) == 0:
            print("destination: {0}".format(dest_cup))

        # The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
        _save = cups[dest_cup]
        cups[dest_cup] = pickup[0]
        cups[pickup[0]] = pickup[1]
        cups[pickup[1]] = pickup[2]
        cups[pickup[2]] = _save
        if debug and (move % debug_interval) == 0:
            print_cups2(cups, current_cup, dest_cup)

        # if debug and (move % debug_interval) == 0:
        #     input()

        # Update the current cup
        current_cup = cups[current_cup]

    print("\n-- final --")
    # print('cups: {0}'.format(cups))
    return cups


def print_cups2(cups, current_cup, dest_cup=None):
    s = 'cups: '
    cup = current_cup
    cutoff = 25
    i = 0
    while i < cutoff and i < len(cups):
        if cup == current_cup:
            s += '({0})'.format(str(cup))
        elif dest_cup and cup == dest_cup:
            s += '[{0}]'.format(str(cup))
        else:
            s += ' {0} '.format(str(cup))
        cup = cups[cup]
        if cup == current_cup:
            break
        i += 1
    print(s)

def print_cups(cups, current_cup, dest_cup=None):
    global debug
    if debug:
        s = 'cups: '
        for i,cup in enumerate(cups):
            if i > 50:
                break
            if cup == current_cup:
                s += '({0})'.format(str(cup))
            elif dest_cup and cup==dest_cup:
                s += '[{0}]'.format(str(cup))
            else:
                s += ' {0} '.format(str(cup))
        print(s)

def main():
    test_input = '389125467'
    puzzle_input = '952316487'
    cups = list(puzzle_input)
    cups = [int(c) for c in cups]

    print("\n--- Part 1 ---")
    part1(cups)

    print("\n--- Part 2 ---")
    part2(cups)

if __name__=="__main__":
    main()