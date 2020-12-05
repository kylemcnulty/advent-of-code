import numpy as np
import time
import sys 
input_filename = "input.txt"

def main(passports):
	valid_passports = 0
	checks = {}

	for p in passports:
		print(p)

		# Reset checks dict
		valid_pass = False
		checks = {
			"all_present": False,
			"byr": False,
			"iyr": False,
			"eyr": False,
			"hgt": False,
			"hcl": False,
			"ecl": False,
			"pid": False,
		}

		if ("byr" in p) and ("iyr" in p) and ("eyr" in p) and ("hgt" in p) and ("hcl" in p) and ("ecl" in p) and ("pid" in p):
			checks["all_present"] = True
		
		if checks["all_present"] == True:
			# Start checking all the values
			if (len(p["byr"])==4) and (1920 <= int(p["byr"]) <= 2002):
				checks["byr"] = True				

			if (len(p["iyr"])==4) and (2010 <= int(p["iyr"]) <= 2020):
				checks["iyr"] = True

			if (len(p["eyr"])==4) and (2020 <= int(p["eyr"]) <= 2030):
				checks["eyr"] = True
			
			# askdfm
			if (p["hgt"][-2:] == "cm") or (p["hgt"][-2:] == "in"):
				field_len = len(p["hgt"])
				hgt_num = int(p["hgt"][:field_len-2])

				if (p["hgt"][-2:] == "cm") and (150 <= hgt_num <= 193):
					checks["hgt"] = True
				elif (p["hgt"][-2:] == "in") and (59 <= hgt_num <= 76):
					checks["hgt"] = True

			if p["hcl"][:1] == "#" and (len(p["hcl"]) == 7):
				chars = p["hcl"][-6:]
				for c in chars:
					if c in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
						checks["hcl"] = True

			if p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
				checks["ecl"] = True

			if len(p["pid"]) == 9:
				checks["pid"] = True

		if False not in checks.values():
			valid_pass = True
			valid_passports += 1

		print(checks)
		print("--> {0}\n".format(valid_pass))

	print(valid_passports)


def load_input_file():
	# Load program values
	passports = []
	with open(input_filename) as f:
		passports = f.read().split('\n\n')

	cleaned_passports = []
	for idx, p in enumerate(passports):
		passports[idx] = p.replace('\r', ' ').replace('\n', ' ').split(' ')
		passport_dict = {}
		for field in passports[idx]:
			if field != "":
				key,value = field.split(':')
				passport_dict[key] = value
		cleaned_passports.append(passport_dict)
		
	return cleaned_passports

if __name__=="__main__":
	passports = load_input_file()
	main(passports)
