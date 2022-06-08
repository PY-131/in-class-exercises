import argparse
import csv 

ALLOWED_EXT = [".csv"]

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', type=argparse.FileType('w'),
                    default=sys.stdout)
parser.parse_args(['data/mock_users_passwords.csv', 'data/output.csv'])


# parser = argparse.ArgumentParser()
# parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin)
# parser.add_argument('outfile', type=argparse.FileType('w'), default=sys.stdout)
# args = parser.parse_args()

# input_data = pd.read_csv(args.infile)
# input_data['password']=input_data['password'].apply(lambda x: randint(5,15)*'*')
# input_data.to_csv(args.outfile)

data = csv.reader(parser.infile)
data = pd.read_csv(parser.infile)




parser.parse_args([])