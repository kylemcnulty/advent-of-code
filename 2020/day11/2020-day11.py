import itertools
import numpy as np
import time
input_filename = "input.txt"

value_map = {
	'.': '.', # floor
	'L': 'L', # empty seat
	'#': '#' # filled seat
}
NUM_ELEMENTS = 0

def main():
	seat_map = load_input_file()
	print("\n---Part 1---")
	part1(seat_map)
	
	# print("\n--Part 2---")
	# part2(adapters)

def part1(seat_map):
	#print("Starting Seat Map", end='')
	#print_matrix(seat_map)
	#print(seat_map)

	y_size, x_size = seat_map.shape
	running = True
	rounds = 1
	new_seat_map = np.copy(seat_map)
	new_seat_map[new_seat_map != ''] =  '' # reset every value in matrix to ''

	previous_map = None

	while running:
		#print("----- Round {0} -----".format(rounds), end='')

		for cy in range(1, y_size-1):
			for cx in range(1, x_size-1):
				#print("--cy:{0}  cx:{1}--".format(cy, cx))

				seat_value = seat_map[cy, cx]
				if seat_value == value_map['.']:
					# Floor space, pass
					new_seat_map[cy][cx] = '.'
				else:
					# Calculated number of occupied seats adjacent to seat of interest
					adjacent = seat_map[cy-1:cy+2,cx-1:cx+2]
					adj_occupied = np.count_nonzero(adjacent == value_map["#"])
					if seat_value == value_map["#"]:
						adj_occupied = adj_occupied - 1

					if adj_occupied == 0:
						new_seat_map[cy, cx] = value_map['#']
					elif (seat_value == value_map['#']) and (adj_occupied >= 4):
						new_seat_map[cy, cx] = value_map['L']
					else:
						pass

				#print("Adjacent occupied: {0}".format(adj_occupied))
				#print_matrix(adjacent)
				#print_matrix(new_seat_map)
				#time.sleep(2.5)

		#print_matrix(new_seat_map)

		# Check whether seat map changed this round
		num_element_changed = np.count_nonzero(new_seat_map != seat_map)
		if num_element_changed == 0:
			print('converged')
			break

		# Prep for next iteration
		seat_map = np.copy(new_seat_map)
		rounds += 1

		

	#print("Ending Seat Map", end='')
	#print_matrix(seat_map)
	num_occupied = np.count_nonzero(seat_map == '#')
	print("*** Result: {0}".format(num_occupied))

def print_matrix(arr):
  for row in arr:
      for element in row:
          print(element, end="")
      print('')

def part2():
	pass

def load_input_file():
	# Load program values
	values = []
	with open(input_filename) as f:
		values = f.read().splitlines()
	global NUM_ELEMENTS 
	NUM_ELEMENTS = x_size * y_size

	seat_map = np.zeros(shape=(y_size+2,x_size+2), dtype=str)
	
	for y in range(0, y_size):
		for x in range(0, x_size):
			seats = []
			seats[:] = values[y]
			seat = values[y][x]
			seat_map[y+1][x+1] = seat # value_map[seat]

	return seat_map

if __name__=="__main__":
	main()
