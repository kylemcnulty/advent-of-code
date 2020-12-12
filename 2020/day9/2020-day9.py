import itertools
input_filename = "input.txt"
PREAMBLE_LENGTH = 25

def main(numbers):
	print("---Part 1---")
	invalid_number = part1(numbers)
	
	print("---Part 2---")
	part2(numbers, invalid_number)

def part1(numbers):
	invalid_number = None
	#print("Numbers: {0}".format(numbers))

	for i,num in enumerate(numbers):
		if i < PREAMBLE_LENGTH:
			continue # skip to the first number after the preamble
		else:
			preamble = numbers[i-PREAMBLE_LENGTH:i]
			#print("\ni={0}  Preamble: {1}".format(i, preamble))

			preamble_combos = list(itertools.combinations(preamble, 2))
			#print("Preamble Combos: {0}".format(preamble_combos))
			preamble_sums = [(c[0]+c[1]) for c in preamble_combos]
			#print("Preamble Sums: {0}".format(preamble_sums))

			if num not in preamble_sums:
				invalid_number = num
				break

	#print("Result: {0}\n".format(num))
	return invalid_number

def part2(numbers, invalid_number):

	for w in range(1, len(numbers)):
		for i in range(0, len(numbers)-w+1):
			cont_sublist = numbers[i:i+w]
			if sum(cont_sublist) == invalid_number:
				#print("Matching Sublist: {0}".format(cont_sublist))
				result = max(cont_sublist) + min(cont_sublist)
				print("Result: {0}".format(result))
				break

def load_input_file():
	# Load program values
	numbers = []
	with open(input_filename) as f:
		numbers = f.read().splitlines()
	
	numbers = [int(x) for x in numbers]
	return numbers

if __name__=="__main__":
	numbers = load_input_file()
	main(numbers)