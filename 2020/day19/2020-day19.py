import re
import pprint
import operator
import time
input_filename = "test_input.txt"
pp = pprint.PrettyPrinter(indent=2)

rules = {}

def	part1(rules, messages):
	pp.pprint(rules)
	
	# Condense the rules into a more readable form
	short_rules = condense_rules(rule_id='0')
	return

def condense_rules(rule_id):
	leaves = ['a', 'b']
	rule = rules[rule_id]
	print("\nCalled function with rule: {0}".format(rule))
	#time.sleep(3)

	if rule in leaves:
		# We're at a leaf 
		print('reached leaf --> returning')
		return rule_id
	else:
		# This rule has an OR statement in it
		print("not a leaf")
		for idx,char in enumerate(rule):
			if char is not ' ':
				print(char)
				s = condense_rules(char)
				print(rules[rule_id][idx])
		# for item in rules:

	print(rules)


def part2(fields, valid_tickets):
	pass

def main():
	rules, messages = load_input_file()

	print("\n--- Part 1 ---")
	part1(rules, messages)	

	#print("\n--- Part 2 ---")
	#result = part2(fields, valid_tickets)	

def load_input_file():
	messages = []
	
	with open(input_filename) as f:
		mode = 'fields'
		for line in f:
			line = line.rstrip()
			if line in ['', None]:
				pass
			else:	
				if ':' in line:
					rule_id, rule = line.split(':')
					rules[rule_id] = rule.lstrip()
				else:
					messages.append(line)	
	
	# Clean up the rules dictionary
	for k, v in rules.items():
		if '"' in v:
			rules[k] = v[1]
		else:
			components = v.split(' ')
			if len(components) == 1:
				rules[k] = v
			else:
				pass
				# if ('|' in components) and len(components) == 5:
				# 	#print(components)
				# 	rules[k] = [
				# 		components[0] + ' ' + components[1],
				# 		components[3] + ' ' + components[4],
				# 	]
				# elif ('|' in components) and len(components) == 3:
				# 	rules[k] = [
				# 		components[0],
				# 		components[2],
				# 	]
				# else:
				# 	rules[k] = v

	return rules, messages

if __name__=="__main__":
	main()