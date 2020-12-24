import pprint
import itertools as it
from collections import Counter
from operator import itemgetter
from statistics import mode
import copy

input_filename = "input.txt"
pp = pprint.PrettyPrinter(indent=2)

def	part1(foods, ingredients, allergens):
	num_allergens = len(allergens)
	allergen_data = [None] * num_allergens

	for i, algn in enumerate(allergens):
		allergen_data[i] = {
			'name': algn,
			'ingredients': [],
			'matching_ingredient': None,
		}
		for food in foods:
			if algn in food['allergens']:
				# Add the ingredients listed for this food to the allergen's list of possible matching ingredients
				allergen_data[i]['ingredients'].extend(food['ingredients'])

	# Sort list of allergens by the number of possible ingredients that could match the allergen. The First sort from least to most number of allergen_data, then we reverse
	allergen_data = sorted(allergen_data, key=lambda k: len(k['ingredients']), reverse=True)
	
	valid_ingredients = [] # valid == ingredients that could possibly match to an allergen
	tmp_allergen_data = copy.deepcopy(allergen_data)
	
	for i, algn in enumerate(tmp_allergen_data):
		counts = Counter(tmp_allergen_data[i]['ingredients']).most_common(5)
		most_common  = counts[0][0]		
		valid_ingredients.append(most_common)
		tmp_allergen_data[i]['matching_ingredient'] = most_common

		# Remove the selected ingredient from the list of possible matching ingredients for every remaining allergen in allergen_data
		for j in range(i, num_allergens):
			if most_common in tmp_allergen_data[j]['ingredients']:
				cleaned_list = [x for x in tmp_allergen_data[j]['ingredients'] if x != most_common]
				tmp_allergen_data[j]['ingredients'] = cleaned_list

	# Count the number of times the invalid ingredients appear in any food's ingredient list
	inert_ingredients = list(set(ingredients) - set(valid_ingredients))
	cnt = 0
	for food in foods:
		for item in inert_ingredients:
			if item in food['ingredients']:
				cnt += food['ingredients'].count(item)

	print('***Result: {0}'.format(cnt))
	print(allergens)
	return allergen_data, inert_ingredients

def	part2(allergen_data, inert_ingredients):
	num_allergens = len(allergen_data)

	# Remove all the inert ingredients from the allergen data
	for i,algn in enumerate(allergen_data):
		#print(algn['name'])
		for inert in inert_ingredients:
				cleaned_list = [x for x in allergen_data[i]['ingredients'] if x != inert]
				allergen_data[i]['ingredients'] = cleaned_list

	# Sort list of allergens by the number of possible ingredients that could match the allergen. The First sort from least to most number of allergen_data, then we reverse
	allergen_data = sorted(allergen_data, key=lambda k: len(k['ingredients']), reverse=True)

	# Compute matchs
	for i, algn in enumerate(allergen_data):
		counts = Counter(allergen_data[i]['ingredients']).most_common(5)
		#print("\n {0}".format(algn['name']))
		#print(counts)
		most_common  = counts[0][0]		
		allergen_data[i]['matching_ingredient'] = most_common

		# Remove the selected ingredient from the list of possible matching ingredients for every remaining allergen in allergen_data
		for j in range(i, num_allergens):
			if most_common in allergen_data[j]['ingredients']:
				cleaned_list = [x for x in allergen_data[j]['ingredients'] if x != most_common]
				allergen_data[j]['ingredients'] = cleaned_list

	# Sort allergen_data alphabetically by the allergen name
	allergen_data = sorted(allergen_data, key=itemgetter('name'))

	result = []
	for algn in allergen_data:
		result.append(algn['matching_ingredient'])

	print(','.join(result))
	
def main():
	foods, ingredients, allergens = load_input_file()

	print("\n--- Part 1 ---")
	allergen_data, inert_ingredients = part1(foods, ingredients, allergens)

	print("\n--- Part 2 ---")
	result = part2(allergen_data, inert_ingredients)	

def load_input_file():
	foods = []
	all_ingredients = set()
	all_allergens = set()
	
	with open(input_filename) as f:
		for line in f:
			ingredients, allergens = line.split('(')
			ingredients = ingredients.rstrip().split(' ')
			allergens = allergens.rstrip().replace('contains ', '').replace(')', '').split(', ')
			f = {'ingredients': ingredients, 'allergens': allergens}
			foods.append(f)
			all_ingredients.update(ingredients)
			all_allergens.update(allergens)

	return foods, list(all_ingredients), list(all_allergens)

if __name__=="__main__":
	main()