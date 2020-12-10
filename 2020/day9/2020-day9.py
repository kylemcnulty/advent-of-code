import itertools
from collections import Counter
input_filename = "input.txt"

def main(adapters, device_rating):
	print("---Part 1---")
	part1(adapters, device_rating)
	
	#print("---Part 2---")
	#part2(adapters)

def part1(adapters, device_rating):
	# Check order
	valid = check_valid(adapters)
	if not valid:
		print("ERROR: Invalid order\n")
		return

	# Count differences between adapters	
	diffs = []
	for i in range(0,len(adapters)-1):
		d = adapters[i+1]["output"] - adapters[i]["output"]
		diffs.append(d)

	diff3_cnt = diffs.count(3)
	diff1_cnt = diffs.count(1)
	result = diff1_cnt * diff3_cnt
	print(result)

def part2(adapters):
	pass

def check_valid(adapters):
	for i in range(0,len(adapters)-1):
		print("i: {0} --> i+1: {1}".format(adapters[i],adapters[i+1]))
		if adapters[i]["output"] not in adapters[i+1]["inputs"]:
			return False
		else:
			return True

def load_input_file():
	# Load program values
	adapter_ratings = []
	with open(input_filename) as f:
		adapter_ratings = f.read().splitlines()
	
	# Precompute the valid inputs for these adapters
	adapter_ratings = [int(x) for x in adapter_ratings]
	adapters = []
	for r in adapter_ratings:
		#r = int(r)
		a = {
			"inputs": list(range(r-3,r)),
			"output": r,
			"type": "adapter"
		}
		adapters.append(a)

	device_rating = max(adapter_ratings) + 3

	adapters.append({
		"inputs": [0],
		"output": 0,
		"type": "outlet"
	})
	adapters.append({
		"inputs": list(range(device_rating-3, device_rating)),
		"output": device_rating,
		"type": "device"
	})

	adapters = sorted(adapters, key=lambda k: k["output"])

	return adapters, device_rating

if __name__=="__main__":
	adapters, device_rating = load_input_file()
	main(adapters, device_rating)