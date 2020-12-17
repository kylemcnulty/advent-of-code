import time
import numpy as np
input_filename = "input.txt"
from functools import reduce


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
	itime = max_bus
	running = True
	bs = list(enumerate(bus_schedule)) # precompute this to doing it every iteration of the while loop

	# product = 1
	# for cb in cleaned_busses:
	# 	product = product * cb
	# print(product)

	while running:
		#print("Time: {0}".format(itime))
		# Rewind to the last time the first bus departed
		itime = itime - max_bus_time_offset
		#print("Rewound time: {0}".format(itime))

		valid_time = True
		for time_offset,bus in bs:
			if (bus is not 'x') and (bus != max_bus):
				time_since_last = (itime + time_offset) % int(bus)
				#print("Bus: {0}  Time since last: {1}".format(bus, time_since_last))
				if time_since_last != 0:
					valid_time = False
					break

		if valid_time:
			running = False

		# Avoid incrementing the itime counter if we're about to exit the loop and calculate the result
		if running:
			itime += max_bus_time_offset # reset to increment of max_bus
			itime += max_bus # increment itime by the largest bus for efficiency

	#print(cnt)
	print("Result: {0}".format(itime))
	return itime

def part2_b(bus_schedule):
	indeces = [bus_schedule.index(bus) for bus in bus_schedule if bus != 'x']
	busses = [int(bus) for bus in bus_schedule if bus != 'x']
	max_bus = max(busses)
	max_bus_time_offset = indeces[busses.index(max_bus)]
	itime = max_bus
	running = True
	indeces, busses = np.asarray(indeces), np.asarray(busses)
	
	while running:
		itime = itime - max_bus_time_offset
		times = list(indeces + itime) # add scalar to vector
		offsets = np.mod(times, busses)
		if np.sum(offsets) == 0:
			break

		itime += max_bus_time_offset # reset to increment of max_bus
		itime += max_bus # increment itime by the largest bus for efficiency
	
	print("Result: {0}".format(itime))
	return itime

def part2_c(bus_schedule):
	#bus_schedule = [int(bus) for bus in bus_schedule]
	#max_bus = max(cleaned_busses) # 
	#max_bus_time_offset = bus_schedule.index(str(max_bus))
	#itime = 1390548191579800
	#running = True
	#bs = list(enumerate(bus_schedule)) # precompute this to doing it every iteration of the while loop

	# Compute coefficients
	n = []
	a = []
	for i,bus in enumerate(bus_schedule):
		if bus is not 'x':
			b_n = int(bus)
			n.append(b_n)
			b_a = int(bus) - i
			a.append(b_a)
	print(n)
	print(a)

	result = chinese_remainder(n,a)
	print(result)
	return result

def part2_d(bus_schedule):
	busses = [(index, int(bus)) for index, bus in enumerate(bus_schedule) if bus != 'x'] # remove 'x' values from list
	time, lcm = 0, 1
	for offset, bus in busses:
		while (time + offset) % bus:
			time += lcm
		lcm *= bus

	print(time)
	return time

def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

def main():
	depart, busses = load_input_file()
	
	#print("\n---Part 1---")
	#part1(depart, busses)
	
	#n=[7,13,59,31,19]
	#a=[0,12,55,25,12]
	#print(chinese_remainder(n,a))

	print("\n--Part 2---")
	result = part2_d(busses)

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
		result = part2_d(ex['schedule'])
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




	# busses = []
	# for i,bus in enumerate(bus_schedule):
	# 	if bus != 'x':
	# 		d = {'bus': int(bus), 'i': i}
	# 		busses.append(d)

	# max_bus = max([x['bus'] for x in bussess])
	# max_bus_time_offset = bus_schedule.index(str(max_bus))
