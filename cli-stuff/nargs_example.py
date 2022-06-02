import argparse

my_parser = argparse.ArgumentParser()

# when -i or --input flag passed, store three integers 
my_parser.add_argument('-i','--input_int', action='store', type=int, nargs=3)
my_parser.add_argument('-s','--input_str', action='store', type=str, nargs=3)

args = my_parser.parse_args()

if args.input_int:
	print(sum(args.input_int))

if args.input_str:
	print(",".join(args.input_str))