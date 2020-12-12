input_filename = "input.txt"

def main(grouped_forms):
	print("---Part 1---")
	part1(grouped_forms)
	
	print("---Part 2---")
	part2(grouped_forms)

def part1(grouped_forms):
	cnt = 0
	for gf in grouped_forms:
		all_questions = ''.join(gf)
		unique_questions = len(set(all_questions))
		cnt += unique_questions

	print("Total Question Count: {0}\n".format(cnt))

def part2(grouped_forms):
	# Reduce to uniques
	cnt = 0

	# forms is a list of all forms for a single group
	for forms in grouped_forms:
		forms_w_unique = [] # will become list of sets
		
		# Convert each form to a set to get only unique questions, then combine them back in a list so
		# we can use set.intersection() with a variable number of sets
		for form in forms:
			form_w_unique = set(form)
			forms_w_unique.append(form_w_unique)
		
		cnt += len(set.intersection(*forms_w_unique))

	print("Total Question Count: {0}\n".format(cnt))

def load_input_file():
	# Load program values
	grouped_forms = []
	with open(input_filename) as f:
		grouped_forms = f.read()
	
	grouped_forms = grouped_forms.split("\n\n")
	for i,f in enumerate(grouped_forms):
		grouped_forms[i] = f.split("\n")

	# Get rid of last blank element of last list - not sure why it's there
	del(grouped_forms[-1][-1])

	return grouped_forms

if __name__=="__main__":
	grouped_forms = load_input_file()
	main(grouped_forms)