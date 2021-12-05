###
input_filename = "input.txt"

def part1(report):
    num_bits = len(report[0])
    gr = '' # gamma rate
    er = '' # epsilon rate

    for bit_pos in range(num_bits):
        cnt_zero, cnt_one = get_counts(report, bit_pos)
        if cnt_zero > cnt_one:
            gr = gr + '0'
            er = er + '1'
        elif cnt_one > cnt_zero:
            gr = gr + '1'
            er = er + '0'

    gr = int(gr, 2)
    er = int(er, 2)
    power_consumption = gr * er
    print('Ans: {0}'.format(power_consumption))

def get_counts(report, bit_pos):
    num_bits = len(report[0])
    cnt_zero, cnt_one = 0,0
    for number in report:
        if number[bit_pos] == '0':
            cnt_zero += 1
        elif number[bit_pos] == '1':
            cnt_one += 1
    return cnt_zero, cnt_one

def filter_numbers(report, bit_pos, bit_val):
    # Return only the numbers in the report that have bit_val in bit_pos
    match_numbers = []
    for number in report:
        if number[bit_pos] == bit_val:
            match_numbers.append(number)
    return match_numbers

def part2(report):
    num_bits = len(report[0])
    ogr = '' # oxygen generator rating
    csr = '' # C02 scrubber rating
    
    # Calculating OGR
    keep = list(report) # create a copy of the report list
    for bit_pos in range(num_bits):
        cnt_zero, cnt_one = get_counts(keep, bit_pos)
        if cnt_zero > cnt_one:
            keep = filter_numbers(keep, bit_pos, '0')
        elif cnt_one > cnt_zero:
            keep = filter_numbers(keep, bit_pos, '1')
        else:
            keep = filter_numbers(keep, bit_pos, '1')
        if len(keep) == 1:
            break
    ogr = int(keep[0], 2)

    keep = list(report) # create a copy of the report list
    # Calculating CSR
    for bit_pos in range(num_bits):
        cnt_zero, cnt_one = get_counts(keep, bit_pos)
        
        if cnt_zero > cnt_one:
            keep = filter_numbers(keep, bit_pos, '1')
        elif cnt_one > cnt_zero:
            keep = filter_numbers(keep, bit_pos, '0')
        else:
            keep = filter_numbers(keep, bit_pos, '0')
        if len(keep) == 1:
            break    
    csr = int(keep[0], 2)

    lsr = ogr * csr # life support rating
    print('Ans: {0}'.format(lsr))

def main():
    report = load_input_file()
    
    print("\n---Part 1---")
    part1(report)
    
    print("\n---Part 2---")
    part2(report)
  
def load_input_file():
    report = []
    with open(input_filename) as f:
        report = f.read().splitlines()
    return report

if __name__=="__main__":
    main()