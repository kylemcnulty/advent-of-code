import itertools

input_filename = "input.txt"

def main():
	with open(input_filename) as f:
		entries = f.read().splitlines()
	entries = [int(el) for el in entries]

	e, f = part1_b(entries)
	print("---Part 1---")
	print("product = {0}\n".format(e*f))

	e, f, g = part2_b(entries)
	print("---Part 2---")	
	print("product = {0}\n".format(e*f*g))

def part1(entries):
	found = False
	for e in entries:
		for f in entries:
			if e + f == 2020:
				found = True
				break
		if found == True:
			break

	assert (e+f) == 2020, "elements don't sum to 2020"
	return e,f

def part2(entries):
	found = False
	for e in entries:
		for f in entries:
			for g in entries:
				if e + f + g == 2020:
					found = True
					break
			if found == True:
				break
		if found == True:
			break

	assert (e+f+g) == 2020, "elements don't sum to 2020"
	return e,f,g 

def part1_a(entries):
	combos = list(itertools.combinations(entries, 2))
	matching = list(filter(lambda el : el[0]+el[1] == 2020, combos))[0]

	e,f = matching[0], matching[1]
	assert (e+f) == 2020, "elements don't sum to 2020"
	return e,f

def part2_a(entries):
	combos = list(itertools.combinations(entries, 3))
	matching = list(filter(lambda el : el[0]+el[1]+el[2] == 2020, combos))[0]

	e,f,g = matching[0], matching[1], matching[2]
	assert (e+f+g) == 2020, "elements don't sum to 2020"
	return e,f,g

def part1_b(entries):
	combos = list(itertools.combinations(entries, 2))
	for el in combos:
		if el[0]+el[1]==2020:
			matching = el
			break

	e,f = matching[0], matching[1]
	assert (e+f) == 2020, "elements don't sum to 2020"
	return e,f

def part2_b(entries):
	combos = list(itertools.combinations(entries, 3))
	for el in combos:
		if el[0]+el[1]+el[2]==2020:
			matching = el
			break

	e,f,g = matching[0], matching[1], matching[2]
	assert (e+f+g) == 2020, "elements don't sum to 2020"
	return e,f,g


if __name__=="__main__":
	main()