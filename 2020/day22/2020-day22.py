from collections import deque
from itertools import islice
input_filename = "input.txt"

num_games = 0

def part1(p1, p2):
    # Continue playing until there are no cards left in one of the player's decks
    r = 1
    while (len(p1) != 0) and (len(p2) != 0):
        print("-- Round {0} --".format(r))
        print("Player 1's deck: {0}".format(p1))
        print("Player 2's deck: {0}".format(p2))
        p1_draw = p1.pop()
        p2_draw = p2.pop()
        print("Player 1 plays: {0}".format(p1_draw))
        print("Player 2 plays: {0}".format(p2_draw))

        if p1_draw > p2_draw:
            print("Player 1 wins the round!")
            p1.appendleft(p1_draw)
            p1.appendleft(p2_draw)
        elif p1_draw < p2_draw:
            print("Player 2 wins the round!")
            p2.appendleft(p2_draw)
            p2.appendleft(p1_draw)
        else:
            print("tie: error")

        r += 1

    print("== Post-game results ==")
    print("Player 1's deck: {0}".format(p1))
    print("Player 2's deck: {0}".format(p2))

    if len(p1) > len(p2):
        winner = p1
    else:
        winner = p2

    result = 0
    for i,card in enumerate(winner):
        result += card * (i+1)

    print("\nResult: {0}".format(result))

def part2(p1, p2):
    winner, p1, p2 = rcombat(p1, p2, game_id=0)

    if winner == 1:
        winner_deck = p1
    elif winner == 2:
        winner_deck = p2

    print("\n == Post-game results ==")
    print("Player 1's deck: {0}".format(p1))
    print("Player 2's deck: {0}".format(p2))

    result = 0
    for i,card in enumerate(winner_deck):
        result += card * (i+1)

    print("\nResult: {0}".format(result))

def rcombat(p1, p2, game_id):
    # Each function call is one game of recursive combat.
    global num_games
    num_games = num_games + 1
    game_id = num_games

    # print("\n=== Game {0} ===".format(game_id))
    game_winner = None
    r = 1
    previous_rounds = deque([])

    while (len(p1) != 0) and (len(p2) != 0) and (game_winner is None):
        round_winner = None
        # print("\n-- Round {0} (Game {1}) --".format(r, game_id))
        # print("Player 1's deck: {0}".format(p1))
        # print("Player 2's deck: {0}".format(p2))        

        # Check if the deck match their configuration in any previous round of this game
        #print("Previous rounds: {0}".format(previous_rounds))
        for pr in previous_rounds:
            #print(previous_rounds)
            if (p1 == pr) or (p2 == pr):
                #print("***Player 1 automatically wins this game")
                game_winner = 1
                break

        # Save the players decks so we can compare later
        previous_rounds.append(p1.copy())
        previous_rounds.append(p2.copy())

        # Players draw cards
        p1_draw = p1.pop()
        p2_draw = p2.pop()
        # print("Player 1 plays: {0}".format(p1_draw))
        # print("Player 2 plays: {0}".format(p2_draw))

        # Check numbers of cards remaining in each deck
        if (len(p1) >= p1_draw) and (len(p2) >= p2_draw):
            # print('Playing a sub-game to determine the winner..')
            new_p1 = list(p1.copy())
            new_p2 = list(p2.copy())
            new_p1 = deque(new_p1[-p1_draw:])
            new_p2 = deque(new_p2[-p2_draw:])

            round_winner = rcombat(new_p1, new_p2, game_id)
    
        # Higher value card wins the round
        if round_winner is None:
            if p1_draw > p2_draw:
                round_winner = 1
            elif p1_draw < p2_draw:
                round_winner = 2
            else:
                print("tie: error")

        if round_winner == 1:
            # print("Player 1 wins round {0} of game {1}!".format(r, game_id))
            p1.appendleft(p1_draw)
            p1.appendleft(p2_draw)
        elif round_winner == 2:
            # print("Player 2 wins round {0} of game {1}!".format(r, game_id))
            p2.appendleft(p2_draw)
            p2.appendleft(p1_draw)

        r += 1
        #input('')

    if game_winner is None:
        if len(p1) > len(p2):
            game_winner = 1
        else:
            game_winner = 2

    # print("The winner of game {0} is player {1}!".format(game_id, game_winner))

    if game_id == 1:
        # Then we're about to exit the entire game
        return game_winner, p1, p2
    else:
        # print("\n...anyway, back to game {0}.".format(game_id))
        return game_winner

def main():
    p1, p2 = load_input_file()

    #print("\n--- Part 1 ---")
    #part1(p1, p2)   
    
    print("\n--- Part 2 ---")
    result = part2(p1, p2)  

def load_input_file():
    p1 = []
    p2 = []
    cards = []

    with open(input_filename) as f:
        cards = f.read().splitlines()

    cards = [c for c in cards if c not in ['', None]]
    p2_start = cards.index('Player 2:')
    p1 = cards[:p2_start]
    p1.remove('Player 1:')
    p2 = cards[p2_start:]
    p2.remove('Player 2:')
    p1 = [int(c) for c in p1]
    p2 = [int(c) for c in p2]
    p1 = deque(p1)
    p1.reverse()
    p2 = deque(p2)
    p2.reverse()

    return p1, p2

if __name__=="__main__":
    main()