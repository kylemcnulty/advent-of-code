input_filename = "testinput.txt"
import numpy as np
import pprint
from itertools import cycle

wins = [0, 0]
board = list(range(1,11))
turn = 0
positions = [0,0]
scores = [0,0]


def part1(start_pos):
    die = cycle(list(range(1,101)))
    board = list(range(1,11))
    scores = [0, 0]
    positions = start_pos.copy()
    turn = 0
    roll_cnt = 0

    while max(scores) < 1000:
        if turn % 2 == 0:
            player = 0
        else:
            player = 1
        
        # Roll the die and track the rolls
        rolls = []
        for roll in range(3):
            rolls.append(next(die))
            roll_cnt += 1
        
        # Calculate where the player needs to move to
        moves = sum(rolls)
        new_pos = ((positions[player] - 1 + moves) % 10) + 1
        positions[player] = new_pos
        scores[player] += new_pos
        turn += 1
        
    losing_score = min(scores)
    ans = losing_score * roll_cnt
    print('Ans: {0}'.format(ans))

def play_game():
    global wins
    global turn
    global positions
    global scores
    print(wins)
    print(scores)
    input()

    if max(scores) >= 21:
        pass
    else:
        if turn % 2 == 0:
            player = 0
        else:
            player = 1
        
        # Roll the die and track the rolls
        rolls = []        
        for roll in [1,2,3]:
            rolls.append(roll)
            
            # Calculate where the player needs to move to
            moves = sum(rolls)
            new_pos = ((positions[player] - 1 + moves) % 10) + 1
            positions[player] = new_pos
            scores[player] += new_pos
            turn += 1

            play_game()

    winner = scores.index(max(scores))
    wins[winner] += 1
    turns = 0
    positions = [0,0]
    scores = [0,0]
    return 
        
        # print('Player {0} rolls {1} and moves to space {2} for a total score of {3}'.format(player+1, rolls, positions[player], scores[player]))

def part2(start_pos):
    global positions
    position = start_pos.copy()

    play_game()
    print(wins)

    # losing_score = min(scores)
    # print('Losing player scored: {0}'.format(losing_score))
    # print('Die was rolled {0} times'.format(roll_cnt))
    # ans = losing_score * roll_cnt
    # print('Ans: {0}'.format(ans))

def main():
    start_pos = load_input_file()
    
    print("\n---Part 1---")
    part1(start_pos)
    
    print("\n---Part 2---")
    part2(start_pos)
  
def load_input_file():
    with open(input_filename) as f:
        p1_start = int(f.readline().strip().split(': ')[1])
        p2_start = int(f.readline().strip().split(': ')[1])
    
    return [p1_start, p2_start]

if __name__=="__main__":
    main()