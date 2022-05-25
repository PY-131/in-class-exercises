
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


"""


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
        count_dict = dict()

        for ch in self.wd:

            if ch in count_dict:
               count_dict[ch] += 1 
            else:
               count_dict[ch] = 1


        #sum(v for k, v in count_dict.items() if k in self.vowels)

        return count_dict











if __name__ == '__main__':
    wd = WordInfo("apple")
    print(wd.count_vowels())
    print(wd.count_consonants())
    print(wd.populate_count_dict())
