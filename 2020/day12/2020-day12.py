import math
input_filename = "input.txt"


def jump_to_waypoint(ship, wp, cmd, val):
	# Move to the waypoint a number of times equal to the value
	diff = [wp[0]-ship[0], wp[1]-ship[1]]
	# Move the ship to waypoint "val" times, make sure waypoint maintains same relative pos to ship
	for i in range(0, val):
		ship = wp.copy()
		wp = [ship[0] + diff[0], ship[1] + diff[1]]
	return ship, wp

def rotate_waypoint(ship, wp, cmd, val):
	# Rotate the waypoint around the ship by "val" degrees
	if cmd is 'R':
		angle = -val
	elif cmd is 'L':
		angle = val

	# Convert angle to clockwise rotation if it's negative to make life easier
	if angle < 0:
		angle = 360 + angle

	s = int(math.sin(math.radians(angle)))
	c = int(math.cos(math.radians(angle)))

	# Translate waypoint back to the origin (ship)
	wp[0] = wp[0] - ship[0] # x
	wp[1] = wp[1] - ship[1] # y

	wp_new = [0,0]
	wp_new[0] = (c * wp[0]) - (s * wp[1])
	wp_new[1] = (s * wp[0]) + (c * wp[1])
	
	# Translate waypoint back to center on ship
	wp = [wp_new[0] + ship[0], wp_new[1] + ship[1]]
	return wp

def move_in_direction(px, py, direction, distance, item):
	if direction is 'N':
		new_y = py + distance
		py = new_y
	elif direction is 'S':
		new_y = py - distance
		py = new_y
	elif direction is 'E':
		new_x = px + distance
		px = new_x
	elif direction is 'W':
		new_x = px - distance
		px = new_x

	result = [px, py]
	return result

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

def part1(actions):
	pos = [0, 0]
	facing = 'E' # either E, S, W, or N, start by facing E.

	for action in actions:
		cmd, val = action[:1], int(action[1:])
		if cmd in ['N', 'S', 'E', 'W']:
			pos = move_in_direction(pos[0], pos[1], cmd, val, "ship")
		elif (cmd is 'L') or (cmd is 'R'):
			new_facing = turn_direction(facing, cmd, val)
			facing = new_facing
		elif cmd is 'F':
			pos = move_in_direction(pos[0], pos[1], facing, val, "ship")
		else:
			print(cmd)
			raise NameError("unknown action")

	man_distance =  abs(pos[0]) + abs(pos[1])
	print("Result: {0}".format(man_distance))

def part2(actions):
	ship = [0, 0]
	wp = [10, 1]

	for action in actions:
		cmd, val = action[:1], int(action[1:])
		if cmd in ['N', 'S', 'E', 'W']:
			wp = move_in_direction(wp[0], wp[1], cmd, val, "waypoint")
		elif cmd in ['L', 'R']:
			wp = rotate_waypoint(ship, wp, cmd, val)
		elif cmd is 'F':
			ship, wp = jump_to_waypoint(ship, wp, cmd, val)
		else:
			raise NameError("unknown action")

	man_distance = abs(ship[0]) + abs(ship[1])
	print("Result: {0}".format(man_distance))

def main():
	actions = load_input_file()
	
	print("\n---Part 1---")
	part1(actions)
	
	print("\n--Part 2---")
	part2(actions)

def load_input_file():
	actions = []
	with open(input_filename) as f:
		actions = f.read().splitlines()
	return actions

if __name__=="__main__":
	main()