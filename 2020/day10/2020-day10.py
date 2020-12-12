import itertools
from collections import Counter
input_filename = "input.txt"

cache = {}

def main(adapters):
	adapters = load_input_file()
	print("\n---Part 1---")
	part1(adapters)
	
	print("\n--Part 2---")
	part2(adapters)

def part1(adapters):
	# Check that adapters list matches stated rules
	valid = check_valid(adapters)
	if not valid:
		raise ValueError("Adapter list is not valid")

	# Calculate differences between adjacent nodes
	diffs = []
	for i in range(0, len(adapters)-1):
		d = adapters[i+1] - adapters[i]
		diffs.append(d)

	result = diffs.count(3) * diffs.count(1)
	print("Result: {0}".format(result))

def check_valid(adapters):
	num_adapters = len(adapters)
	for i in range(0, num_adapters-1):
		diff = abs(adapters[i+1] - adapters[i])
		if diff > 3:
			return False
	return True # if loop completes, then adapters list is valid

def part2(adapters):
	num_leaves = traverse_tree(adapters[0], adapters)
	print("Result: {0}".format(num_leaves))

def traverse_tree(root, adapters):
	total_num_leaves = 0
	children = find_valid_adapters(root, adapters)
	if len(children) == 0:
		return 1 # Return 1 to indicate we hit a leaf node
	else:
		for c in children:
			if c in cache:
				num_leaves = cache[c]
			else:
				num_leaves = traverse_tree(c, adapters)
				cache[c] = num_leaves
			total_num_leaves += num_leaves

	return total_num_leaves

def find_valid_adapters(rating, adapters):
	valid_adapters = []
	for a in adapters:
		if rating in range(a-3, a):
			valid_adapters.append(a)

	return valid_adapters

def load_input_file():
	# Load program values
	adapters = []
	with open(input_filename) as f:
		adapters = f.read().splitlines()
	
	# Precompute the valid inputs for these adapters
	adapters = [int(x) for x in adapters]
	adapters.append(0) # add the outlet
	adapters.append(max(adapters) + 3) # add the device
	adapters.sort()
	return adapters

if __name__=="__main__":
	main()