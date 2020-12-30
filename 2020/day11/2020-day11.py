import itertools
import numpy as np
import time
input_filename = "input.txt"

# Globals
y_size = None
x_size = None

def main():
	seat_map = load_input_file()

	#print("\n---Part 1---")
	#part1(seat_map)
	
	print("\n--Part 2---")
	part2(seat_map)

def part1(seat_map):
	rounds = 1
	new_seat_map = seat_map.copy()
	while True:
		for cy in range(0, y_size):
			for cx in range(0, x_size):
				# print("\n--cy:{0}  cx:{1}--".format(cy, cx))
				seat_value = seat_map[(cx, cy)]
				if seat_value == '.':
					# Floor space, pass
					new_seat_map[(cx,cy)] = '.'
				else:
					adj_occupied = check_adjacent_pt1(seat_map, cx, cy)
					if (seat_value == 'L') and (adj_occupied == 0):
						new_seat_map[(cx, cy)] = '#'
					elif (seat_value == '#') and (adj_occupied >= 4):
						new_seat_map[(cx, cy)] = 'L'
					else:
						pass

		# Check whether seat map changed this round
		if seat_map == new_seat_map:
			print('converged')
			break

		# Prep for next iteration
		seat_map = new_seat_map.copy()
		rounds += 1

	num_occupied = list(seat_map.values()).count('#')
	print("*** Result: {0}".format(num_occupied))

def check_adjacent_pt1(seat_map, cx, cy):
	# Calculated number of occupied seats adjacent to seat of interest
	adj_occupied = 0
	adjacent_offsets = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
	for ao in adjacent_offsets:
		x = cx + ao[0]
		y = cy + ao[1]
		if ((x, y) in seat_map) and seat_map[(x, y)] == '#':
			adj_occupied += 1

	return adj_occupied

def part2(seat_map):
	rounds = 1
	new_seat_map = seat_map.copy()
	while True:
		for cy in range(0, y_size):
			for cx in range(0, x_size):
				# print("\n--cy:{0}  cx:{1}--".format(cy, cx))
				seat_value = seat_map[(cx, cy)]
				if seat_value == '.':
					# Floor space, pass
					new_seat_map[(cx,cy)] = '.'
				else:
					adj_occupied = check_adjacent_pt2(seat_map, cx, cy)
					if (seat_value == 'L') and (adj_occupied == 0):
						new_seat_map[(cx, cy)] = '#'
					elif (seat_value == '#') and (adj_occupied >= 5):
						new_seat_map[(cx, cy)] = 'L'
					else:
						pass

		# Check whether seat map changed this round
		if seat_map == new_seat_map:
			print('converged')
			break

		# Prep for next iteration
		seat_map = new_seat_map.copy()
		rounds += 1

	num_occupied = list(seat_map.values()).count('#')
	print("*** Result: {0}".format(num_occupied))

def check_adjacent_pt2(seat_map, cx, cy):
	# Calculated number of occupied seats adjacent to seat of interest
	adj_occupied = 0
	adjacent_offsets = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
	for ao in adjacent_offsets:
		level = 1
		while True:
			x = cx + level*ao[0]
			y = cy + level*ao[1]
			if ((x, y) in seat_map):
				if seat_map[(x, y)] == '.':
					pass
				elif seat_map[(x, y)] == '#':
					adj_occupied += 1
					break
				elif seat_map[(x, y)] == 'L':
					break
			else:
				break
			level += 1
	
	return adj_occupied

def print_seatmap(seat_map):
	for y in range(y_size):
		for x in range(x_size):
			print(seat_map[(x, y)], end="")
		print('')

def load_input_file():
	# Load program values
	global y_size
	global x_size
	values = []
	with open(input_filename) as f:
		values = f.read().splitlines()
	
	y_size = len(values)
	x_size = len(values[0])
	seat_map = {}
	for y in range(0, y_size):
		for x in range(0, x_size):
			seat_map[(x,y)] = values[y][x]

	return seat_map

if __name__=="__main__":
	main()
