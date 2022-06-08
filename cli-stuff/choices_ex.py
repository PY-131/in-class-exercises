import argparse

my_parser = argparse.ArgumentParser()

# restrict input to be between 1 and 5 with choices=
my_parser.add_argument('-a','--another_example', action='store', type=int, choices=range(1, 5))
my_parser.add_argument('-e','--example', action='store_true')
args = my_parser.parse_args()

# we can use vars to turn a class into a dictionary for easy processing
print(vars(args))
print(args.another_example)
print(args.example)


# vars without args is locals() which shows us what variables are in our current scope
# print(locals())

# python3 choices_ex.py -a 4