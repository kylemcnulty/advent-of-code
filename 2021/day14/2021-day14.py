input_filename = 'input.txt'
from blist import blist
import pprint

def part1(polymer, rules):
    steps = 20
    print('Template: {0}'.format(polymer))
    new_polymer = polymer.copy()

    for step in range(1, steps+1):
        num_insertions = 0
        plength = len(polymer)

        for i in range(plength - 1):
            sub = polymer[i:i+2] 
           
            for pair, insertedEl in rules:
                if pair == sub:
                    new_polymer.insert(i+num_insertions+1, insertedEl)
                    num_insertions += 1

        polymer = new_polymer.copy()
        print('Polymer is {0} long after step {1}'.format(len(polymer), step))

    most, least = most_frequent(polymer), least_frequent(polymer)
    most_cnt, least_cnt = polymer.count(most), polymer.count(least)
    ans = most_cnt - least_cnt
    print('Ans: {0}'.format(ans))

def part2(polymer, rules):
    steps = 40
    print('Template: {0}'.format(polymer))

    # Convert polymer to different data structure
    dpolymer = {}
    for i in range(len(polymer)-1):
        p = ''.join([polymer[i], polymer[i+1]])
        if p in dpolymer:
            dpolymer[p] += 1
        else:
            dpolymer[p] = 1
    new_dpolymer = dpolymer.copy()

    # Convert rules to a different data structure
    drules = {}
    for pair, insertedEl in rules:
        pair = ''.join(pair)
        drules[pair] = insertedEl
    
    elements = {}
    unique_elements = set(list(''.join(drules.keys())))
    for ue in unique_elements:
        elements[ue] = polymer.count(ue)

    for step in range(1, steps+1):
        for pair, cnt in dpolymer.items():
            if pair in drules and dpolymer[pair] > 0:
                newPair1 = pair[0] + drules[pair]
                newPair2 = drules[pair] + pair[1]

                if newPair1 != newPair2:
                    if newPair1 in new_dpolymer:
                        new_dpolymer[newPair1] += cnt
                    else:
                        new_dpolymer[newPair1] = cnt
                    
                    if newPair2 in new_dpolymer:
                        new_dpolymer[newPair2] += cnt
                    else:
                        new_dpolymer[newPair2] = cnt

                    new_dpolymer[pair] -= cnt
                    elements[drules[pair]] += cnt
                else:
                    if newPair1 in new_dpolymer:
                        new_dpolymer[newPair1] += 2*cnt
                    else:
                        new_dpolymer[newPair1] = 2*cnt
                    new_dpolymer[pair] -= 2*cnt
                    elements[drules[pair]] += 2*cnt
            else:
                continue

        dpolymer = new_dpolymer.copy()

    most, least = max(elements.values()), min(elements.values())
    ans = most - least
    print('Ans: {0}'.format(ans))

def most_frequent(List):
    return max(set(List), key = List.count)

def least_frequent(List):
    return min(set(List), key = List.count)

def main():
    polymer,rules = load_input_file()
    
    #print("\n---Part 1---")
    #part1(polymer, rules)

    print("\n---Part 2---")
    part2(polymer, rules)
  
def load_input_file():
    p = None
    rules = []
    
    with open(input_filename) as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            else:
                if i == 0:
                    p = blist(line)
                else:
                    rule = line.split(' -> ')
                    pair = blist(rule[0])
                    el = rule[1]
                    rule = blist([pair, el])
                    rules.append(blist(rule))

    # print(rules)
    return p, rules

if __name__=="__main__":
    main()