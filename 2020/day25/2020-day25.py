input_filename = 'input.txt'

def part1(public_keys):
    subject = 7
    loop_sizes = []
    for pk in public_keys:
        loops = 0
        number = 1
        while number != pk: # loops <= 8:
            number = number * subject
            number = number % 20201227
            loops += 1
        loop_sizes.append(loops)

    encrypt_key = 1
    subject = public_keys[0]
    loop_size = loop_sizes[1]
    for l in range(loop_size):
        encrypt_key = encrypt_key * subject
        encrypt_key = encrypt_key % 20201227

    print("Result: {0}".format(encrypt_key))

def main():
    public_keys = load_input_file()

    print("\n--- Part 1 ---")
    part1(public_keys)

def load_input_file():
    public_keys = []
    with open(input_filename) as f:
        for line in f:
            public_keys.append(int(line))
    return public_keys

if __name__=="__main__":
    main()