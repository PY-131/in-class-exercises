import unittest
import csv

from text_analysis import WordInfo


TEST_CASES = "data/test_cases.csv"

class WordInfoTests(unittest.TestCase):

	def setUp(self):
		self.word_obj = WordInfo("apple")
		self.word_obj2 = WordInfo("APple")


	def test_count_vowels(self):
		self.assertEqual(self.word_obj.count_vowels(), 2, "the result of count vowels should be 2")
		self.assertEqual(self.word_obj2.count_vowels(), 2, "the result of count vowels should be 2")

		# if you want bulk test with a csv file
		with open(TEST_CASES) as f:
			data = csv.reader(f)
			for entry in data:
				self.assertEqual(WordInfo(entry[0]).count_vowels(), int(entry[1]), f"input: {entry[0]}, output: {entry[1]}")



	def test_count_consonants(self):
		self.assertEqual(self.word_obj.count_consonants(), 3, "the result of count vowels should be 3")
		self.assertEqual(self.word_obj2.count_consonants(), 3, "the result of count vowels should be 2")

	def test_populate_count_dict(self):
		self.assertDictEqual(self.word_obj.populate_count_dict(), {'a': 1, 'p': 2, 'l': 1, 'e': 1})





if __name__ == '__main__':
	unittest.main()