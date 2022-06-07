import argparse
from text_analysis import WordInfo
from pprint import pprint as pp

"""
Word Info CLI 

examples: 
python3 word-info.py 'heey' --letter_count 
python3 word-info.py 'heey' --vowel_count 
python3 word-info.py 'heey' --consonants_count 

"""

parser = argparse.ArgumentParser() 
parser.add_argument("WORD")
parser.add_argument("-lc","--letter_count", action="store_true", help="Counts letters")
parser.add_argument("-vc","--vowel_count", action="store_true", help="Counts vowels")
parser.add_argument("-cc","--consonants_count", action="store_true", help="counts consonants")
parser.add_argument("-s", "--sorted", action="store", help="sort output", choices= ["ASC", "DESC"])
args = parser.parse_args()


wd = WordInfo(args.WORD)

if args.letter_count:
	res = wd.populate_count_dict()	

	if args.sorted:
		sorting_ = True if args.sorted == "DESC" else False
		res = sorted(res.items(), key=lambda x: x[1], reverse=sorting_)

	for k,v in res:
		print(f"letter: {k}, frequency: {v}")

if args.vowel_count:
	print(f"Vowl Count: {wd.count_vowels()}")

if args.consonants_count:
	print(f"Consonant Count: {wd.count_consonants()}")

