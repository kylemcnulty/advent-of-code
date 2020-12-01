import numpy as np
import time
import sys 
input_filename = "input.txt"

example_inputs = [
	[
		['R8','U5','L5','D3'],
		['U7','R6','D4','L4']
	],
	[
		['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
		['U62','R66','U55','R34','D71','R55','D58','R83']
	],
	[
		['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
		['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
	],
]

def main(wire_inputs):
	# Load program values
	x_size = 30000
	y_size = 30000

	wire_maps = [] # wire map matrices going in here
	for wire in wire_inputs:
		# Create the new wire map
		wire_map = np.zeros(shape=(x_size,y_size), dtype=np.int32)
		port_x = int(x_size/2) # central port x (column) location
		port_y = int(y_size/2) # central port y (row) location 
		wire_map[port_y][port_x] = 2 # set the central port to 2
		cx = port_x
		cy = port_y
		steps = 0

		# 1 for wire location; 2 for central port; 0 for no wire
		# Set the wires 
		for instruct in wire:
			print('Instruction: {}'.format(instruct))
			direction = str(instruct[:1])
			distance = int(instruct[1:])
			submap_to_update = None

			if direction is 'R':
				new_x = cx + distance
				submap_to_update = wire_map[cy,cx+1:new_x+1]
				cx = new_x
			elif direction is 'L':
				new_x = cx - distance
				submap_to_update = wire_map[cy,new_x:cx]
				cx = new_x
			elif direction is 'U':
				new_y = cy - distance
				submap_to_update = wire_map[new_y:cy,cx]
				cy = new_y
			elif direction is 'D':
				new_y = cy + distance
				submap_to_update = wire_map[cy+1:new_y+1,cx]
				cy = new_y
			else:
				raise NameError("unknown wire instruction")
			
			# left and up moves are confused
			if direction is 'U' or direction is 'L':
				val = steps + distance 
			elif direction is 'R' or direction is 'D':
				val = steps + 1

			#print(submap_to_update)
			for x in np.nditer(submap_to_update, op_flags=['readwrite']):
				if x == 0: # the wire hasn't cross this location before
					x[...] = val
				if x > 0:
					pass
				
				if direction is 'U' or direction is 'L':
					val -= 1
				elif direction is 'R' or direction is 'D':
					val += 1
				steps += 1

			# Optional values to print
			#print(submap_to_update)
			#print('Cursor: X={} Y={}\n'.format(cx, cy))
			
		wire_maps.append(wire_map)

		np.set_printoptions(threshold=10000000, linewidth=200)
		#print(wire_map)
	
	# Do element wise multiplication to figure where intersections are
	merged_wire_map = wire_maps[0] * wire_maps[1]
	#print("\nMerged Wire Map")
	#print(merged_wire_map)

	# Get locations of non-zero elements in the merged wire map
	intersections = np.transpose(np.nonzero(merged_wire_map > 0))
	print("\nIntersections are:")
	# Remove central port from list of intersections
	central_port = np.where(np.all(intersections==[port_x,port_y],axis=1))
	intersections = np.delete(intersections, central_port, 0)

	distances = []
	signal_delays = []
	for inter_x,inter_y in intersections:
		# Calculate distance from central port
		distance = abs(inter_x - port_x) + abs(inter_y - port_y)
		signal_delay = wire_maps[0][inter_x,inter_y] + wire_maps[1][inter_x,inter_y]
		print('   [{}, {}]    distance={}    signal_delay={} steps'.format(inter_x, inter_y, distance, signal_delay))
		distances.append(distance)
		signal_delays.append(signal_delay)

	min_distance = min(distances)
	min_signal_delay = min(signal_delays)
	print()
	print('Distance from central port to closest intersection: {}'.format(min_distance))
	print('Signal delay from central port to closest intersection: {}\n'.format(min_signal_delay))	

def load_input_file():
	# Load program values
	with open(input_filename) as f:
		values_txt = f.read().splitlines()
		#values = list(map(int, values_txt))
	
	wire_inputs = []
	for strings in values_txt:
		wire_inputs.append(strings.split(','))
	
	return wire_inputs

if __name__=="__main__":
	wire_inputs = load_input_file()
	#wire_inputs = example_inputs[2]
	
	main(wire_inputs)
	
	#part1()
	#part2()