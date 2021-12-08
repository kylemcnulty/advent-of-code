input_filename = "input.txt"

def part12(fish_by_age, days):
    for day in range(1, days+1):
        new_fish_by_age = [0]*9
        for age,num_fish in enumerate(fish_by_age):
            if age == 0:
                new_fish_by_age[6] = num_fish
                new_fish_by_age[age] = 0
                new_fish_by_age[8] += num_fish # create new children
            else:
                new_fish_by_age[age-1] += fish_by_age[age]

        fish_by_age = new_fish_by_age.copy()

    num_fish = sum(fish_by_age)
    print("Ans: {0} fish after {1} days".format(num_fish, days))

def main():
    fish_by_age = load_input_file()
    
    print("\n---Part 1---")
    part12(fish_by_age, days=80)
    
    print("\n---Part 2---")
    part12(fish_by_age, days=256)
  
def load_input_file():
    fishes = []
    
    with open(input_filename) as f:
        line = f.readline().strip()
        fishes = line.split(',')
        fishes = list(map(int, fishes))

    # Reformat the fish population to a list of counts, where each list index represents an age and each value 
    # is the number of fish with that age.
    fish_by_age = [0]*9 # Fish can be any age from 0-8, so there are nine possible age values
    for fish in fishes:
        fish_by_age[fish] += 1

    return fish_by_age

if __name__=="__main__":
    main()