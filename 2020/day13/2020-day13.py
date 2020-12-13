import time
input_filename = "test_input.txt"

def part1(depart, busses):
	busses = [int(bus) for bus in busses if bus != 'x'] # remove 'x' values from list
	itime = depart # minutes
	running = True
	earliest_bus = None

	while running:
		for bus in busses:
			time_since_last = itime % bus
			if time_since_last == 0:
				earliest_bus = bus
				running = False # exit while loop
				break # out of for loop

		# Avoid incrementing the itime counter if we're about to exit the loop and calculate the result
		if running:
			itime += 1

	result = earliest_bus * (itime - depart)
	print("Result: {0}".format(result))

def part2(bus_schedule):
	cleaned_busses = [int(bus) for bus in bus_schedule if bus != 'x'] # remove 'x' values from list
	max_bus = max(cleaned_busses) # 
	max_bus_time_offset = bus_schedule.index(str(max_bus))

	# busses = []
	# for i,bus in enumerate(bus_schedule):
	# 	if bus != 'x':
	# 		d = {'bus': int(bus), 'i': i}
	# 		busses.append(d)

	# max_bus = max([x['bus'] for x in bussess])
	# max_bus_time_offset = bus_schedule.index(str(max_bus))

	#print(max_bus_time_offset)
	#first_bus = int(bus_schedule[0])
	#first_bus_time_offset = bus_schedule.index(str(first_bus))
	itime = 0
	running = True
	#print(itime)

	while running:
		#print("Time: {0}".format(itime))
		# Rewind to the last time the first bus departed
		itime = itime - max_bus_time_offset
		#print("Rewound time: {0}".format(itime))

		valid_time = True
		for time_offset,bus in enumerate(bus_schedule):
			if bus is not 'x':
				time_since_last = (itime + time_offset) % int(bus)
				#print("Bus: {0}  Time since last: {1}".format(bus, time_since_last))
				if time_since_last != 0:
					valid_time = False

		if valid_time:
			running = False

		# Avoid incrementing the itime counter if we're about to exit the loop and calculate the result
		if running:
			itime += max_bus_time_offset # reset to increment of max_bus
			itime += max_bus # increment itime by the largest bus for efficiency

		#print("Valid? {0}\n".format(valid_time))
		#time.sleep(1)

	print("Result: {0}".format(itime))
	return itime

def main():
	depart, busses = load_input_file()
	
	#print("\n---Part 1---")
	#part1(depart, busses)
	
	print("\n--Part 2---")
	result = part2(busses)

	examples = [
		{'schedule': ['17','x','13','19'], 'result': 3417},
		{'schedule': ['67','7','59','61'], 'result': 754018},
		{'schedule': ['67','x','7','59','61'],'result': 779210},
		{'schedule': ['67','7','x','59','61'], 'result': 1261476},
		{'schedule': ['1789','37','47','1889'], 'result': 1202161486},
	]

	print("\nTesting Part 2 Solution")
	for ex in examples:
		print(ex)
		result = part2(ex['schedule'])
		if result == ex['result']:
			print("Passed")
		else:
			print("failed")
		print()

def load_input_file():
	data = []
	with open(input_filename) as f:
		data = f.read().splitlines()
	
	depart = int(data[0])
	busses = data[1].split(',')
	return depart, busses

if __name__=="__main__":
	main()