input_filename = "input.txt"

example_input = [
	14,
	1969,
	100756
]

def main():
	with open(input_filename) as f:
		masses = f.read().splitlines()
	masses = [int(el) for el in masses]	

	fuels = []
	for m in masses:
		fuels.append(calc_fuel(m))
	
	print(sum(fuels))

def calc_fuel(mass):
	print('running calc_fuel with mass = {}'.format(mass))
	fuel = int(mass/3) - 2

	if fuel < 0:
		fuel = 0
	else:
		fuel = fuel + calc_fuel(fuel)

	return fuel

if __name__=="__main__":
	main()