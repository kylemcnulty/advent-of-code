import pprint

input_filename = "input.txt"
pp = pprint.PrettyPrinter(indent=2)

# Globals
bags = {}

def main():
	load_input_file()

	print("\n---Part 1---")
	part1()
	
	print("\n--Part 2---")
	part2()

def part1():
	global bag
	for bag_color, bag_data in bags.items():
		result = check_for_gold(bag_color)
		bags[bag_color]['contains_gold'] = result
	
	# Count how many bags can contain gold
	cnt = 0
	for bag in bags:
		if (bag != 'shiny gold') and bags[bag]['contains_gold']:
			cnt += 1
	print("Result: {0}".format(cnt))

def check_for_gold(bag):
	result = False

	# Check if we have already computed whether 'bag' can contain shiny gold bags.
	if bags[bag]['contains_gold'] is not None:
		result = bags[bag]['contains_gold']
	else:
		for cbag in bags[bag]['contents']:
			if cbag == 'shiny gold':
				# If 'bag' can directly contain shiny gold bags, then 'bag' can contain shiny gold bags, and we can skip the rest of 'bag's contents.
				result = True
				break
			else:
				result = check_for_gold(cbag)
				if result:
					# If one of the 'cbags' can contain gold, then 'bag' can contain gold, and we can skip the rest of 'bags' contents.
					break
				else:
					pass

	return result

def part2():
	num = count_bags('shiny gold')
	print("Result: {0}".format(num))

def count_bags(bag):
	num_bags = 0
	for cbag,cnum in bags[bag]['contents'].items():
		result = count_bags(cbag)
		num_bags += cnum + (cnum*result)
	return num_bags

def load_input_file():
	# Load program values
	global bags

	with open(input_filename) as f:
		for line in f:
			line = line.strip()
			color, contents = line.split(' bags contain ')
			bags[color] = {'contains_gold': None, 'contents': {}}
			if contents != 'no other bags.':
				contents = contents.split(',')
				for c in contents:
					c = c.strip()
					num, adj, col, scrap = c.split(' ')
					num = int(num)
					value = '{0} {1}'.format(adj.strip(), col.strip())
					bags[color]['contents'][value] = num

if __name__=="__main__":
	main()
