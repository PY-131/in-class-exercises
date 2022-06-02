# argv.py
import sys

# print(f"Name of the script      : {sys.argv[0]=}")
# print(f"Arguments of the script : {sys.argv[1:]=}")


def parse_args(args):

	"""
	using all()  
	"""

	# if all i.isdigit() is true for args, then return True
	if all(i.isdigit() for i in args):
		return sum(int(i) for i in args)

	# if all i.isalpha() is true for args, then return True
	elif all(i.isalpha() for i in args):
		return ",".join(args)
	else:
		raise Exception("Enter either all numbers or all letters! ")

	return None


def parse_args_alt(args):

	"""
	using lists 
	"""

	digits = []
	letters = []

	for i in args:

		if i.isdigit():
			digits.append(i)
		elif i.isalpha():
			letters.append(i)

	if len(digits) == len(args):
		return sum(map(int, digits))
	elif len(letters) == len(args):
		return ",".join(letters)
	else:
		raise Exception("Enter either all numbers or all letters! ")

if __name__ == '__main__':
	print(parse_args_alt(sys.argv[1:]))