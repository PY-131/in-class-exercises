import argparse 

#instantiate the parser
parser = argparse.ArgumentParser()

# add arguments (positional argument echo)
parser.add_argument("echo")
parser.add_argument("echo2")
#parses args, turns them into a python obj
args = parser.parse_args()

#now able to access it like a python obj or class
print(args.echo)
print(args.echo2)