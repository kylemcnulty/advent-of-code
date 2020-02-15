import time
from  colorama import Fore, Back, Style

class Program():
	def __init__(self, program_values):
		self.memory = program_values
		self.pointer = 0

	def run(self, verbose=False):
		program_length = len(self.memory)

		while self.pointer < program_length:
			# Print latest version of program
			if verbose is True:
				print(self)

			if self.memory[self.pointer] == 1:
				self.add()
			elif self.memory[self.pointer] == 2:
				self.multiply()
			elif self.memory[self.pointer] == 99:
				break
			else:
				raise ValueError("unknown op code")

			program_length = len(self.memory)
	
			# Add short delay so verbose output is readable
			if verbose is True:
				time.sleep(0.25)

	def update(self, address, value):		
		max_address = len(self.memory) - 1

		if address > max_address:
			# then expand list to have length of index_to_overwrite-1 and null fill
			new_mem = [None] * (address - max_address)
			self.memory.extend(new_mem)
		else:
			pass

		self.memory[address] = value 

	def add(self):
		param1 = self.memory[self.pointer + 1]
		param2 = self.memory[self.pointer + 2]
		param3 = self.memory[self.pointer + 3]
		
		instruction_result = self.memory[param1] + self.memory[param2] 
		self.update(address=param3, value=instruction_result)
		self.pointer += 4

	def multiply(self):
		param1 = self.memory[self.pointer + 1]
		param2 = self.memory[self.pointer + 2]
		param3 = self.memory[self.pointer + 3]
		
		instruction_result = self.memory[param1] * self.memory[param2] 
		self.update(address=param3, value=instruction_result)
		self.pointer += 4

	def __str__(self):
		output = "["
		for address,value in enumerate(self.memory):
			if address == self.pointer:
				output += Back.RED + str(value) + Style.RESET_ALL
			else:
				output += str(value)
		
			# Print comma after all but last value	
			if address < (len(self.memory) - 1):
				output = output + ','

		output += "]"
		return output

	def __repr__(self):
		return str(self)
