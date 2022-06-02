import argparse

my_parser = argparse.ArgumentParser()

# restrict input to be between 1 and 5 with choices=
my_parser.add_argument('-a', action='store', type=int, choices=range(1, 5))
args = my_parser.parse_args()

# we can use vars to turn a class into a dictionary for easy processing
print(vars(args))

# vars without args is locals() which shows us what variables are in our current scope
# print(locals())