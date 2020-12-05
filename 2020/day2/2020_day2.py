input_filename = "input.txt"

def main():
    with open(input_filename) as f:
        entries = f.read().splitlines()

    print("---Part 1---")
    part1(entries)
    
    print("---Part 2---")
    part2(entries)

def part1(entries):
    count_valid = 0
    for el in entries:
        min_occ = int(el.split("-")[0])
        max_occ = int(el.split(" ")[0].split("-")[1])
        letter = el.split(" ")[1][0:1]
        psk = el.split(":")[1].lstrip(" ")
        
        occ = psk.count(letter)
        if occ >= min_occ and occ <= max_occ:
            count_valid += 1

    print(count_valid)

def part2(entries):
    count_valid = 0
    for el in entries:
        pos_a = int(el.split("-")[0])
        pos_b = int(el.split(" ")[0].split("-")[1])
        letter = el.split(" ")[1][0:1]
        psk = el.split(":")[1].lstrip(" ")
        
        matching_pos = 0
        if psk[pos_a-1] == letter:
            matching_pos += 1
        if psk[pos_b-1] == letter:
            matching_pos += 1

        if matching_pos == 1:
            count_valid +=1

    print(count_valid)

if __name__=="__main__":
    main()