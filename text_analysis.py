
"""


i.e. word examples
word1 = "functionality"
word2 = "apple"
word3 = "orange"


that has the following functionality (as methods):
1. Takes a word as input
2. counts the vowels of a given word vowels: "aeiou"
3. counts the consonants of a given word "all the other letters that are not vowels"

4. Add tests using unittest

EXTRA:
Implement a way to read each word from  a text file.


Modify the code to do the following:

1) instead of reading one word, it reads a text file of words
2) implement a method called get_word_frequency() that counts the frequency of the words in the text
3) implement tests using pytest

"""


from pprint import pprint as pp
from collections import Counter 


class TextAnalysis:

    def __init__(self, file_):
        self.file_ = file_

    def get_frequency(self, n=5):

        freq = {}
        with open(self.file_) as f:
            data = f.read().split()
            for wd in data:
                wd = wd.lower()
                #wd = replace_punct(wd)
                if wd.isalpha():
                    if wd in freq:
                        freq[wd] += 1 
                    else:
                        freq[wd] = 1
        return sorted(freq.items(), key=lambda x:x[1], reverse=True)[:n]

    def get_freq_with_counter(self, n=5):

        res = Counter()
        with open(self.file_) as f:
            data = f.read().split()
            for wd in data:
                wd = wd.lower()
                res[wd] += 1
        return res.most_common(n)

class WordInfo:

    vowels = 'aeiou'

    def __init__(self, word):
        self.wd = word.lower()


    def count_vowels(self):
        # count = 0
        # for ch in self.wd:
        #     if ch in self.vowels:
        #         count += 1
        # return count
        return sum(1 for ch in self.wd if ch in self.vowels)


    def count_consonants(self):
        # count = 0
        # for ch in self.wd:
        #     if ch not in self.vowels:
        #         count += 1
        # return count
        #return sum(1 for ch in self.wd if ch not in self.vowels)
        return len(self.wd) - self.count_vowels()


    def populate_count_dict(self):
        """ 
        get count of each letter
        """
        count_dict = {}

        for ch in self.wd:

            if ch in count_dict:
               count_dict[ch] += 1 
            else:
               count_dict[ch] = 1


        #sum(v for k, v in count_dict.items() if k in self.vowels)

        return count_dict



if __name__ == '__main__':
    # wd = WordInfo("apple")
    # print(wd.count_vowels())
    # print(wd.count_consonants())
    # print(wd.populate_count_dict())

    print(TextAnalysis("data/text1.txt").get_freq_with_counter())
    print(TextAnalysis("data/text1.txt").get_frequency())
