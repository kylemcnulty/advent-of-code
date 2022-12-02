input_filename = "testinput2.txt"
import pprint

MASTER_DIGITS = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('adbefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg')
}

def part1(notes):
    num_digits = 0
    for entry in notes:
        for digit in entry["outputs"]:
            d_un = [len(val) for key,val in MASTER_DIGITS.items() if key in (1, 4, 7, 8)]
            if len(digit) in d_un:
                num_digits += 1
    print('Ans: {0} digits with a unique number of segments'.format(num_digits))

def part2(notes):

    for entry in notes:
        ed = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }
        # Create master to entry map
        segmap = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None,
        }
        for s in entry['signals']:
            # print(s)
            
            # Match all the easy ones to start
            if len(s) == 2:
                ed[1] = s
            elif len(s) == 4:
                ed[4] = s
            elif len(s) == 3:
                ed[7] = s
            elif len(s) == 7:
                ed[8] = s

        # Guess at the segment mapping options based on unique numbers
        segmap['a'] = ed[7] - ed[1]
        segmap['c'] = ed[1] & ed[7]
        segmap['f'] = ed[1] & ed[7]
        segmap['b'] = ed[4].difference(ed[1])
        segmap['d'] = ed[4].difference(ed[1])
        segmap['e'] = ed[8].difference(ed[7]).difference(ed[4])
        segmap['g'] = ed[8].difference(ed[7]).difference(ed[4])

        # Two Options
        bd_options = list(segmap['b'])
        cf_options = list(segmap['c'])
        eg_options = list(segmap['e'])

        segmap['a'] = str(list(segmap['a'])[0])
        
        segmap['b'] = str(bd_options[0])
        segmap['d'] = str(bd_options[1])
        segmap['c'] = str(cf_options[0])
        segmap['f'] = str(cf_options[1])
        segmap['e'] = str(eg_options[0])
        segmap['g'] = str(eg_options[1])

        print('Segmap')
        pprint.pprint(segmap)
        # print(ed)

        break


def main():
    notes = load_input_file()
    
    print("\n---Part 1---")
    part1(notes)
    
    print("\n---Part 2---")
    part2(notes)
  
def load_input_file():
    notes = []
    
    with open(input_filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            signals, outputs = line.split(' | ')
            signals, outputs = signals.split(' '), outputs.split(' ')
            notes.append({
                'signals': [set(s) for s in signals],
                'outputs': [set(o) for o in outputs]
            })
    return notes

if __name__=="__main__":
    main()