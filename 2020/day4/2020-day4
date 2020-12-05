import numpy as np
import time
import sys 
input_filename = "input.txt"

def main(map_rows):
	n_cols = len(map_rows[0])
	n_rows = len(map_rows)
	print(n_cols)
	print(n_rows)

	# slope inputs
	slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)] 

	for slope in slopes:
		slope_right = slope[0]
		slope_down = slope[1]
		num_trees = 0
		col_idx = 0

		for row_idx in range(0, n_rows, slope_down):
			found_tree = "no"
			# Skip first iteration of outerloop to correctly start at (0,0)
			if (row_idx == 0):
				pass
			else:
				col_idx += slope_right
				if col_idx > (n_cols-1):
					col_idx = col_idx - (n_cols)
				
				# Check whether tree is present
				if map_rows[row_idx][col_idx] == "#":
					found_tree = "yes"
					num_trees += 1

				#print("row: {0}	  col: {1}   tree: {2}".format(row_idx, col_idx, found_tree))

		print("slope: {0}  num_trees: {1}".format(slope, num_trees))

def load_input_file():
	# Load program values
	map_rows = []
	with open(input_filename) as f:
		map_rows = f.read().splitlines()
		#values = list(map(int, values_txt))
	
	return map_rows

if __name__=="__main__":
	map_rows = load_input_file()
	main(map_rows)
