input_filename = "input.txt"

def main(instructions):
	# print("---Part 1---")
	# part1(instructions)

	print("---Part 2---")
	part2(instructions, op_change=False)
	
def part1(instructions):
	acc = 0 # accumulator, global var for op-code program
	num_instructions = len(instructions)
	i = 0
	visited_inst = [False] * num_instructions

	while i < num_instructions:
		op = instructions[i][:3]
		arg = int(instructions[i][4:])

		print("---- {} ----".format(instructions[i]))
		
		# Mark this instruction as visited
		visited_inst[i] = True

		if op == 'nop':
			i += 1
			continue # skip the rest of this iteration and continue to next iteration of loop
		elif op == 'acc':
			i += 1
			acc += arg
		elif op == 'jmp':
			i += arg

		# Check if we've visited the next instruction (the one we're about to visit on next iteration of loop)
		# If we're about to visit an instruction that we've already visit, stop and print the accumulator value
		if visited_inst[i] == True:
			print("Accumulator value: {0}".format(acc))
			break

def part2(instructions, op_change=False):
	print("\nEntered Function w/ {0} instructions".format(len(instructions)))
	print(instructions)
	
	num_instructions = len(instructions)
	i = 0
	acc = 0
	visited_inst = [False] * num_instructions

	while i < num_instructions:
		op = instructions[i][:3]
		arg = instructions[i][4:]
		
		print("{0}, i={1}, acc={2}".format(instructions[i], i, acc))

		# Mark this instruction as visited
		visited_inst[i] = True


		if (op == 'jmp' or op == 'nop') and (op_change == False):
			if op == 'jmp':
				print("Changing jmp --> nop")
				new_instructions = instructions.copy()
				new_instructions[i] = 'nop {0}'.format(arg)
				exited = part2(new_instructions, op_change=True)
			elif op == 'nop':
				print("Changing nop --> jmp")
				new_instructions = instructions.copy()
				new_instructions[i] = 'jmp {0}'.format(arg)	
				exited = part2(new_instructions, op_change=True)

			if exited == 1:
				return 1
			
		# Follow instruction
		if op == 'nop':
			i += 1
			continue # skip the rest of this iteration and continue to next iteration of loop
		elif op == 'acc':
			i += 1
			acc += int(arg)
		elif op == 'jmp':
			i += int(arg)

		# Check if we've visited the next instruction (the one we're about to visit on next iteration of loop)
		# If we're about to visit an instruction that we've already visit, stop and print the accumulator value
		try:
			if visited_inst[i] == True:
				print("Found Infinite Loop. Returning")
				break
		except IndexError:
			print("Found Infinite Loop. Returning")
			break

	if i == num_instructions:
		print("PROGRAM TERMINATED: tried to execute instruction immediately after the last in the file")
		print("Accumulator value: {0}".format(acc))
		return 1
	else:
		print("PROGRAM DID NOT TERMINATE")
		return 0

def load_input_file():
	# Load program values
	instructions = []
	with open(input_filename) as f:
		instructions = f.read().splitlines()
	return instructions

if __name__=="__main__":
	instructions = load_input_file()
	main(instructions)