import intcode
import time
import sys

input_filename = "input.txt"

example_input = [
	[1,9,10,3,2,3,11,0,99,30,40,50],
	[1,0,0,0,99],
	[2,3,0,3,99],
	[2,4,4,5,99,0],
	[1,1,1,4,99,5,6,0,99],
]

def examples():
	# Load program values
	values = example_input[4]

	# Create Program
	program = intcode.Program(values)

	# Run program
	program.run(verbose=True)

	print("\nFinal Program State: ", end='')
	print(program)

def part1():
	# Load program values
	with open(input_filename) as f:
		values_txt = f.read().split(',')
		values = list(map(int, values_txt))

	# Create Program
	program = intcode.Program(values)

	# Modify program memory according to instructions
	program.memory[1] = 12
	program.memory[2] = 2

	# Run program
	program.run(verbose=False)

	print("\nFinal Program State: ", end='')
	print(program)

def part2():
	# Load program values
	with open(input_filename) as f:
		values_txt = f.read().split(',')
		values = list(map(int, values_txt))

	for noun in range(100):
		for verb in range(100):
			# Create Program
			program = intcode.Program(values.copy())

			# Modify program memory according to instructions
			program.memory[1] = noun
			program.memory[2] = verb

			# Run program
			program.run()

			if program.memory[0] == 19690720:
				answer = 100 * noun + verb
				print("Answer is: {}".format(answer))
				return
	
	print("no answer found")

if __name__=="__main__":
	#examples()
	#part1()
	part2()