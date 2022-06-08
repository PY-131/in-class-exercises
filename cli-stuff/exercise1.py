
import random 
import argparse 
"""
Write a python CLI that randomly selects a number from 1 to 5 when --random flag is passed
when the random flag is not passed, use a positional argument to restrict the inputted number to be between 1 - 5

1. when --random is passed 
2. when --random is not passed 


python3 exercise1.py --number 3

-> 3 

python3 exercise1.py --number 6

-> throws an error, input must be between 1-5


python3 exercise1.py --random

-> 3 


python3 exercise1.py --random

-> 5 

""" 
MIN=1
MAX = 5

parser = argparse.ArgumentParser()

parser.add_argument("-n","--number", type=int, choices=range(1,6)) 
parser.add_argument("-r","--random", help="Generates a number between 1-5", action="store_true")
parser.add_argument("-mx", "--max_random", help="Add max value to number generation", type=int)


args = parser.parse_args()

if args.number:
	print(f"Inputted number: {args.number}")
if args.random:

	if args.max_random:
		MAX = args.max_random

	print(f"random number: {random.randint(MIN, MAX)}")
