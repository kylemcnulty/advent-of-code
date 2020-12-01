import numpy as np
import time
import sys 
input_filename = "input.txt"

example_inputs = [112233, 123444, 111122]

def main(possible_pwds):
	matching_pwds = []
	for num in possible_pwds:
		num = str(num)
		if check_two_adjacent(num) is True:
			if check_not_decrease(num) is True:
				matching_pwds.append(num)
			else:
				pass
		else:
			continue

	print(matching_pwds)
	print("\nThere are {} matching passwords\n".format(len(matching_pwds)))

def check_adjacent(num):
	# Are there two adjacent digits that are the same
	result = False
	for index in range(len(num)-1):
		if int(num[index]) == int(num[index+1]):
			result = True
		else:
			pass
	return result

def check_not_decrease(num):
	# Going from left to right, the digits never decrease; they only increase or stay the same
	result = True
	for index in range(len(num)-1):
		if int(num[index]) > int(num[index + 1]):
			result = False
		else:
			pass
	return result

def check_two_adjacent(num):
	# Are there two adjacent digits that are the same
	max_index = len(num) - 1
	start_i = 0
	end_i = 1
	double_substrings = 0

	while start_i < max_index:
		while (end_i <= max_index):
			if (num[start_i] == num[end_i]):
				end_i += 1
			else:
				break

		num_repeats = end_i - start_i
		if num_repeats == 1:
			msg = "I'm not a repeat"
		elif num_repeats == 2:
			msg = "I'm repeated twice"
			double_substrings += 1
		elif num_repeats > 2:
			msg = "I'm repeated more than twice"
		else:
			msg = "error"

		#print("Substring: {}    {}".format(num[start_i:end_i], msg))

		start_i = end_i
		end_i = start_i + 1

	if double_substrings >= 1:
		return True
	else:
		return False

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
	possible_pwds = range(307237, 769058)
	#possible_pwds = [example_inputs[2]]
	main(possible_pwds)
	