import numpy as np
import time
import sys 
import math
input_filename = "input.txt"

# Tell numpy not truncate matrices when printing them
np.set_printoptions(threshold=np.inf)

def main(passes):
	pass_ids = []
	seat_map = np.zeros(shape=(128,8), dtype=np.int32)

	for p in passes:
		row_range = [0,127]
		col_range = [0,7]
		pass_row = None
		pass_col = None
		
		row_codes = p[:6]
		final_row_code = p[6:7]
		col_codes = p[7:9]
		final_col_code = p[9:10]
		
		#print("Row Codes: {0}  Final Row Code: {1}".format(row_codes, final_row_code))
		for rc in row_codes:
			delta = row_range[1] - row_range[0]
			lower_half = [row_range[0], row_range[0] + math.floor(delta/2)]
			upper_half = [row_range[0] + math.floor(delta/2) + 1, row_range[1]]

			if rc == "F":
				row_range = lower_half
			elif rc == "B":
				row_range = upper_half

			#print("Code: {0}   Row Range: {1}".format(rc, row_range))

		if final_row_code == "F":
			pass_row = row_range[0]
		elif final_row_code == "B":
			pass_row = row_range[1]

		#print("Pass Row: {0}".format(pass_row))

		#print("Col Codes: {0}  Final Col Code: {1}".format(col_codes, final_col_code))
		for cc in col_codes:
			delta = col_range[1] - col_range[0]
			lower_half = [col_range[0], col_range[0] + math.floor(delta/2)]
			upper_half = [col_range[0] + math.floor(delta/2) + 1, col_range[1]]

			if cc == "L":
				col_range = lower_half
			elif cc == "R":
				col_range = upper_half

			#print("Code: {0}   Col Range: {1}".format(cc, col_range))

		if final_col_code == "L":
			pass_col = col_range[0]
		elif final_col_code == "R":
			pass_col = col_range[1]

		#print("Pass Col: {0}".format(pass_col))

		pass_id = (pass_row * 8) + pass_col
		#print("Pass ID: {0}\n".format(pass_id))
		pass_ids.append(pass_id)

		# Fill in the seat map
		seat_map[pass_row][pass_col] = 1

	print("------Max Pass ID: {0}------\n".format(max(pass_ids)))

	print(seat_map)

def load_input_file():
	# Load program values
	passes = []
	with open(input_filename) as f:
		passes = f.read().splitlines()
	
	return passes

if __name__=="__main__":
	passes = load_input_file()
	main(passes)
