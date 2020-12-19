import re
import pprint
import operator
input_filename = "input.txt"
pp = pprint.PrettyPrinter(indent=2)

def	part1(fields, tickets):
	tser = 0
	valid_tickets = []
	for t in tickets:
		valid = True
		nums_valid = []
		for num in t['numbers']:
			# Check if the number is valid for any field
			num_valid = False
			for f in fields:
				if num in f['rules'][0]:
					num_valid = True
				elif num in f['rules'][1]:
					num_valid = True
			
			nums_valid.append(num_valid)
			if not num_valid:
				# if the number isn't valid, log it so we can compute ticket scanning error rate
				tser += num

		t['numbers_valid'] = nums_valid
		t['valid'] = all(nums_valid)
		if t['valid']:
			valid_tickets.append(t)

	print("Result: {0}".format(tser))
	return valid_tickets

def part2(fields, valid_tickets):
	num_fields = len(fields)
	num_tickets = len(valid_tickets)
	for t in valid_tickets:
		valid = True
		nums_valid = []
		for i_num,num in enumerate(t['numbers']):
			# Check if the number is valid for any field
			num_valid = False
			for f in fields:
				if num in f['rules'][0]:
					f['occurences'][i_num] += 1
				elif num in f['rules'][1]:
					f['occurences'][i_num] += 1
				else:
					pass

	# Create the options matrix for each position/field in the ticket
	field_data = [None] * num_fields
	for pos in range(num_fields):
		field_data[pos] = {
			'pos': pos,
			'options': []
		}
		for field in fields:
			if field['occurences'][pos] == num_tickets:
				field_data[pos]['options'].append(field['name'])

	# Sort and print the matrix
	field_data = sorted(field_data, key=lambda k: len(k['options']))
	for pos in range(num_fields):
		options = field_data[pos]['options']
		num_options = len(options)
		print("Pos: {0}   # Options: {1}  --> {2}".format(pos, num_options, options))
	
	# Solve the options matrix
	field_positions = [None] * num_fields
	for i,field in enumerate(field_data):
		options = field['options']
		pos = field['pos']
		if len(options) == 1:
			selection = options[0]
			print("Position {0} == '{1}'".format(pos, selection))
			
			field_positions[pos] = selection
			for j in range(i, num_fields):
				if selection in field_data[j]['options']:
					field_data[j]['options'].remove(selection)
	
	#print(field_positions)
	# Calculate result
	result = 1
	for pos,field in enumerate(field_positions):
		if field.startswith('departure'):
			value = valid_tickets[0]['numbers'][pos]
			result *= value
			print(value)

	print("Result: {0}".format(result))
	return valid_tickets

def main():
	fields, tickets = load_input_file()

	print("\n--- Part 1 ---")
	valid_tickets = part1(fields, tickets)	
	print("Down to {0} valid tickets from {1} total tickets".format(len(valid_tickets), len(tickets)))

	print("\n--- Part 2 ---")
	result = part2(fields, valid_tickets)	

def load_input_file():
	tickets = []
	fields = []
	
	with open(input_filename) as f:
		mode = 'fields'
		for line in f:
			line = line.rstrip()
			if line in ['', None, 'your ticket:', 'nearby tickets:']:
				mode = 'tickets'
				continue
			else:
				if mode == 'fields':
					ranges = line.split(':')[1].rstrip()
					range1 = ranges.split(' or ')[0].lstrip()
					range2 = ranges.split(' or ')[1].lstrip()
					range1 = [int(range1.split('-')[0]), int(range1.split('-')[1])]
					range2 = [int(range2.split('-')[0]), int(range2.split('-')[1])]
					field = {
						'name': line.split(':')[0],
						'rules': [range(range1[0], range1[1]+1), range(range2[0], range2[1]+1)],
						'occurences': None
					}
					fields.append(field)
				elif mode == 'tickets':
					nums = line.split(',')
					ticket = {
						'valid': None,
						'numbers': [int(n) for n in nums]
					}
					tickets.append(ticket)

	# Add a list of zeros with length equal to the number of fields on the ticket, for tracking occurences in part 2
	num_fields = len(tickets[0]['numbers'])
	for i in range(len(fields)):
		fields[i]['occurences'] = [0] * num_fields
	
	return fields, tickets

if __name__=="__main__":
	main()