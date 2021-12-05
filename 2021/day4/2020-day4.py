import pprint

input_filename = "input.txt"
NUM_BOARDS = 0
BOARD_SIZE = (5, 5)

def check_for_first_winner(boards):
    winner = False
    for bid in range(NUM_BOARDS):
        # Check all of the columns for a winner
        for x in range(BOARD_SIZE[0]):
            winner = True
            for y in range(BOARD_SIZE[1]):
                if boards[(bid, x, y)]['marked'] == False:
                    winner = False
                    break
            if winner:
                break
        if winner:
            break

        # Check all of the rows for a winner
        for y in range(BOARD_SIZE[1]):
            winner = True
            for x in range(BOARD_SIZE[0]):
                if boards[(bid, x, y)]['marked'] == False:
                    winner = False
                    break
            if winner:
                break
        if winner:
            break
    
    if winner:
        return bid
    else:
        return None

def check_for_any_winners(boards):
    winners = []
    for bid in range(NUM_BOARDS):
        # Check all of the columns for a winner
        for x in range(BOARD_SIZE[0]):
            complete_col = True
            for y in range(BOARD_SIZE[1]):
                if boards[(bid, x, y)]['marked'] == False:
                    complete_col = False
                    break
            if complete_col:
                if bid not in winners:
                    winners.append(bid)
                break
        
        # Check all of the rows for a winner
        for y in range(BOARD_SIZE[1]):
            complete_row = True
            for x in range(BOARD_SIZE[0]):
                if boards[(bid, x, y)]['marked'] == False:
                    complete_row = False
                    break
            if complete_row:
                if bid not in winners:
                    winners.append(bid)
                break
    
    return winners

def sum_unmarked(boards, board_id):
    unmarked_sum = 0
    for x in range(BOARD_SIZE[0]):
        for y in range(BOARD_SIZE[1]):
            el = boards[(board_id, x, y)]
            if el['marked'] == False:
                unmarked_sum += el['val']
    return unmarked_sum

def part1(draws, boards):
    # Find the first winning board of bingo
    for draw in draws:
        # Iterate through every position on every board to find the matching elements
        for bid in range(NUM_BOARDS):
            for x in range(BOARD_SIZE[0]):
                for y in range(BOARD_SIZE[1]):
                    if boards[(bid, x, y)]['val'] == draw:
                        boards[(bid, x, y)]['marked'] = True

        winner = check_for_first_winner(boards)
        if winner:
            break

    if winner is not None:
        un_sum = sum_unmarked(boards, winner)
        final_score = draw * un_sum
        print("\nBoard {0} wins with Draw {1}".format(winner, draw))
        print("Ans: {0}".format(final_score))

def part2(draws, boards):
    # Find the last winning board of bingo
    game_winners = []
    for draw in draws:
        # Iterate through every position on every board to find the matching elements
        for bid in range(NUM_BOARDS):
            for x in range(BOARD_SIZE[0]):
                for y in range(BOARD_SIZE[1]):
                    if boards[(bid, x, y)]['val'] == draw:
                        boards[(bid, x, y)]['marked'] = True

        draw_winners = check_for_any_winners(boards)
        for dw in draw_winners:
            if dw not in game_winners:
                game_winners.append(dw)

        if len(game_winners) == NUM_BOARDS:
            last_winner = game_winners[len(game_winners)-1]
            break
    
    un_sum = sum_unmarked(boards, last_winner)
    final_score = draw * un_sum
    print("\nThe last winner is board {0} with draw {1}".format(last_winner, draw))
    print("Ans: {0}".format(final_score))

def main():
    draws, boards = load_input_file()
    
    print("\n---Part 1---")
    part1(draws, boards)
    
    print("\n---Part 2---")
    part2(draws, boards)
  
def load_input_file():
    draws = None
    boards = {}
    global NUM_BOARDS
    
    with open(input_filename) as f:
        draws = f.readline().strip().split(',')
        draws = list(map(int, draws))
        bid, x, y = 0, 0, 0
        while True:
            line = f.readline()
            if not line:
                break
            elif line == '\n':
                y = 0
                for i in range(5):
                    line = f.readline()
                    for el in line.strip().split():
                        boards[(bid, x, y)] = {
                            'val': int(el),
                            'marked': False,
                        }
                        x += 1
                    x = 0
                    y += 1
                bid += 1

    NUM_BOARDS = bid
    return draws, boards

if __name__=="__main__":
    main()