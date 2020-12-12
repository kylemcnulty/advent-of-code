import itertools
import numpy as np
import time
import math
input_filename = "input.txt"

def main():
	np.set_printoptions(threshold=10000000, linewidth=200)
	actions = load_input_file()
	
	#print("\n---Part 1---")
	#part1(actions)
	
	print("\n--Part 2---")
	part2(actions)

def part1(actions):
	map_size = (30000, 30000) # y,x
	game_map = np.zeros(shape=map_size, dtype=np.int32)
	start_pos = (int(map_size[0]/2), int(map_size[1]/2))
	game_map[start_pos[0]][start_pos[1]] = 2 # mark the starting poisition with 2
	py, px = start_pos # position trackers
	facing = 'E' # either E, S, W, or N, start by facing E.

	for action in actions:
		cmd, val = action[:1], int(action[1:])

		if cmd in ['N', 'S', 'E', 'W']:
			py, px = move_in_direction(game_map, px, py, cmd, val, "ship")
		elif (cmd is 'L') or (cmd is 'R'):
			new_facing = turn_direction(facing, cmd, val)
			facing = new_facing
		elif cmd is 'F':
			py, px = move_in_direction(game_map, px, py, facing, val, "ship")
		else:
			print(cmd)
			raise NameError("unknown action")

	man_distance =  abs(py - start_pos[0]) + abs(px - start_pos[1])
	print("Result: {0}".format(man_distance))

def part2(actions):
	map_size = (80000, 80000) # y,x
	game_map = np.zeros(shape=map_size, dtype=np.int32)
	
	# Create starting positions for the ship and waypoint. Waypoint starts 10 units east and 1 unit north
	# relative to the ship. Mark the starting positions with special digits
	origin = (int(map_size[0]/2), int(map_size[1]/2))
	ship_start_pos = origin
	wp_start_pos = (ship_start_pos[0] - 1, ship_start_pos[1] + 10)
	game_map[ship_start_pos[0], ship_start_pos[1]] = 1 # set the ships starting point  to 2
	game_map[wp_start_pos[0], wp_start_pos[1]] = 3 # set the waypoint starting point to 3
	
	# Create variables to track position of the ship and waypoint
	ship = np.asarray(ship_start_pos)
	wp = np.asarray(wp_start_pos)
	# ship_facing = 'E' # either E, S, W, or N, start by facing E.

	readable_ship = np.subtract(ship, origin)
	readable_wp = np.subtract(wp, origin)
	print("***Ship: {0}   Waypoint: {1}\n".format(readable_ship, readable_wp))

	for action in actions:
		print("Action: {0}".format(action))
		cmd, val = action[:1], int(action[1:])

		if cmd in ['N', 'S', 'E', 'W']:
			# Move the waypoint by the given value
			wp = move_in_direction(game_map, wp[1], wp[0], cmd, val, "waypoint")
		elif (cmd is 'L') or (cmd is 'R'):
			# Rotate the waypoint around the ship by "val" degrees
			if cmd is 'L':
				angle = -val
			elif cmd is 'R':
				angle = val

			# Convert angle to clockwise rotation if it's negative to make life easier
			if angle < 0:
				angle = 360 + angle

			s = math.sin(math.radians(angle))
			c = math.cos(math.radians(angle))

			# Translate waypoint back to the origin (ship)
			wp = np.subtract(wp, ship)

			wp_new = np.asarray([0, 0])
			wp_new[0] = wp[1] * s + wp[0] * c # y
			
			wp_new[1] = wp[1] * c - wp[0] * s # x

			wp = np.add(wp_new, ship)

			#new_facing = turn_direction(facing, cmd, val)
			#facing = new_facing
		elif cmd is 'F':
			# Move to the waypoint a number of times equal to the value
			diff = np.subtract(wp, ship)
			# Move the ship to waypoint "val" times, make sure waypoint maintains same relative pos to ship
			for i in range(0, val):
				ship = wp
				wp = np.add(ship, diff)
		else:
			pass
			#print(cmd)
			#raise NameError("unknown action")

		readable_ship = np.subtract(ship, origin)
		readable_wp = np.subtract(wp, origin)
		print("Ship: {0}   Waypoint: {1}\n".format(readable_ship, readable_wp))

	#print_matrix(game_map)
	print(ship)
	man_distance =  abs(ship[1] - ship_start_pos[1]) + abs(ship[0] - ship_start_pos[0])
	print("Result: {0}".format(man_distance))

	pass

def move_in_direction(game_map, px, py, direction, distance, item):
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

	if item is 'ship':
		#submap_to_update[...] = 2 # set whole submap to 1 to indicate ship path
		game_map[py, px] = 2
	elif item is 'waypoint':
		#submap_to_update[...] = 4
		game_map[py, px] = 4
	return np.asarray((py, px))

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

def load_input_file():
	# Load program values
	actions = []
	with open(input_filename) as f:
		actions = f.read().splitlines()

	return actions

if __name__=="__main__":
	main()