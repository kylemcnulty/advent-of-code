import itertools
import numpy as np
import time
input_filename = "input.txt"

def main():
	np.set_printoptions(threshold=10000000, linewidth=200)
	actions = load_input_file()
	
	print("\n---Part 1---")
	part1(actions)
	
	# print("\n--Part 2---")
	# part2(adapters)

def part1(actions):
	x_size = 30000
	y_size = 30000
	game_map = np.zeros(shape=(x_size,y_size), dtype=np.int32)
	start_y, start_x = int(y_size/2), int(x_size/2) # central port x (column) location
	game_map[start_y][start_x] = 2 # set the central port to 2
	py, px = start_y, start_x # position counters for x and y
	facing = 'E' # either E, S, W, or N

	for action in actions:
		cmd, val = action[:1], int(action[1:])
		#print("--- Action: {0} ---".format(action))
		#print("Facing: {0}".format(facing))

		if cmd in ['N', 'S', 'E', 'W']:
			py, px = move_in_direction(game_map, px, py, cmd, val)
		elif (cmd is 'L') or (cmd is 'R'):
			new_facing = turn_direction(facing, cmd, val)
			facing = new_facing
		elif cmd is 'F':
			py, px = move_in_direction(game_map, px, py, facing, val)
		else:
			print(cmd)
			raise NameError("unknown action")

		#print_matrix(game_map)
		#print()

	man_distance = abs(px-start_x) + abs(py-start_y)
	print("Result: {0}".format(man_distance))

def move_in_direction(game_map, px, py, direction, distance):
	if direction is 'N':
		new_y = py - distance
		submap_to_update = game_map[new_y:py, px]
		py = new_y
	elif direction is 'S':
		new_y = py + distance
		submap_to_update = game_map[py+1:new_y+1, px]
		py = new_y
	elif direction is 'E':
		new_x = px + distance
		submap_to_update = game_map[py, px+1:new_x+1]
		px = new_x
	elif direction is 'W':
		new_x = px - distance
		submap_to_update = game_map[py, new_x:px]
		px = new_x

	submap_to_update[...] = 1 # set whole submap to 1 to indicate ship path
	return py, px

def turn_direction(facing, turn_direction, degrees):
	num_quarter_turns = int(degrees/90)
	right_turn_order = ['N', 'E', 'S', 'W']
	left_turn_order = ['N', 'W', 'S', 'E']
	
	if turn_direction == 'R':
		turn_order = right_turn_order
	elif turn_direction == 'L':
		turn_order = left_turn_order

	facing_index = turn_order.index(facing)
	new_facing_index = facing_index + num_quarter_turns
	new_facing_index = new_facing_index % 4
	new_facing = turn_order[new_facing_index]
	return new_facing

def print_matrix(arr):
  for row in arr:
      for element in row:
          print(element, end="")
      print('')

def part2():
	pass

def load_input_file():
	# Load program values
	actions = []
	with open(input_filename) as f:
		actions = f.read().splitlines()

	return actions

if __name__=="__main__":
	main()