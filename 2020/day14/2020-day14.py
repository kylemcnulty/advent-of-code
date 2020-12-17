import re
input_filename = "input.txt"

def part1(instructions):
	mask = None
	mem = {}
	for instruct in instructions:
		i_type = instruct[:3]
		#print("Instruction: {0}".format(instruct))
		if i_type == 'mas':
			# Update the bitmask
			mask = instruct.split('=')[1].lstrip()
			mask = list(mask)
			#print(mask)
		elif i_type == 'mem':
			# Write a new value to memory, after applying the bit mask
			address = int(re.search('\[(.+?)\]', instruct).group(1))
			value = int(instruct.split('=')[1].lstrip())
			bin_value = list("{:036b}".format(value))

			for i in range(36):
				if mask[i] is 'X':
					pass
				else:
					bin_value[i] = mask[i]

			new_bin_value = "".join(bin_value)
			new_int_value = int(new_bin_value, 2)
			
			mem[address] = new_int_value

	result = sum(mem.values())
	print(result)
	return result

def part2(instructions):
	mask = None
	floating_bits = []
	mem = {}

	for instruct in instructions:
		i_type = instruct[:3]
		print("Instruction: {0}".format(instruct))
		if i_type == 'mas':
			# Update the bitmask
			mask = instruct.split('=')[1].lstrip()
			mask = list(mask)
			num_floating = mask.count('X')
			idx_floating = [i for i, x in enumerate(mask) if x == 'X']

			# Create range of floating value based on number of floating values
			floating_bits = []
			for num in range(0, 2**num_floating):
				b = bin(num)[2:].zfill(num_floating)
				b = list(b)
				floating_bits.append(b)

		elif i_type == 'mem':
			# Write a new value to memory. Adjust the memory address with the bitmask
			address = int(re.search('\[(.+?)\]', instruct).group(1))
			bin_address = list("{:036b}".format(address))
			value = int(instruct.split('=')[1].lstrip())

			for i in range(36):
				if mask[i] is '0':
					pass # don't modify the bit
				elif mask[i] is '1':
					bin_address[i] = mask[i]
				elif mask[i] is 'X':
					pass # we'll handle these later

			# Create all the variations of addresses based on floating bits
			addresses = []
			#print(floating_bits)
			for fbits in floating_bits:
				new_address = bin_address.copy()
				for cnt,ifloat in enumerate(idx_floating):
					new_address[ifloat] = fbits[cnt]
				addresses.append(new_address)
				#print("".join(new_address))

			#print(addresses)
			for a in addresses:
				bin_a = "".join(a)
				int_a = int(bin_a, 2)
				mem[int_a] = value

	result = sum(mem.values())
	print(result)
	return result

def main():
	instructions = load_input_file()

	#print("\n---Part 1---")
	#part1(instructions)	
	print("\n--Part 2---")
	result = part2(instructions)

def load_input_file():
	instructions = []
	with open(input_filename) as f:
		instructions = f.read().splitlines()
	return instructions

if __name__=="__main__":
	main()