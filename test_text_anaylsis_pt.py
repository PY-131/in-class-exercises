import pytest, csv

from text_analysis import WordInfo, get_word_counts
@pytest.mark.wordinfo
def test_count_vowels(word_info_obj):
	assert word_info_obj.count_vowels() == 2

@pytest.mark.wordinfo
def test_count_consonants(word_info_obj):
	assert word_info_obj.count_consonants() == 3

@pytest.mark.wordinfo
def test_populate_count_dict(word_info_obj):
	assert word_info_obj.populate_count_dict() ==  {'a': 1, 'p': 2, 'l': 1, 'e': 1}


@pytest.mark.wordinfo
@pytest.mark.parametrize("word, count", [('apple', 2), ('orange', 3), ('peach', 2), ('pinapple', 3), ('eee', 3)])
def test_count_vowels(word, count):
	assert WordInfo(word).count_vowels() == count


@pytest.mark.wordinfo_bulk
def test_vowel():
	with open('data/test_cases.csv') as f:
		data = csv.reader(f)
		for row in data:
			assert WordInfo(row[0]).count_vowels() == int(row[1])


@pytest.mark.textanalysis
def test_get_frequency(text_analysis_obj, stop_words_list):
	result1 = text_analysis_obj.get_frequency() 
	expected1 = [('the', 12), ('of', 12), ('a', 9), ('and', 8), ('programming', 7)]
	
	result2 = text_analysis_obj.get_frequency(stop_words = stop_words_list) 
	expected2 = [('programming', 7), ('computer', 3), ('process', 3), ('code', 3), ('software', 3)]	

	assert result1 == expected1
	assert result2 == expected2

@pytest.mark.textanalysis
def test_get_counter_frequency(text_analysis_obj):
	result = text_analysis_obj.get_freq_with_counter() #compute_word_counts()
	expected = [('the', 12), ('of', 12), ('a', 9), ('and', 8), ('programming', 7)]
	assert result == expected 

@pytest.mark.textanalysis
def test_word_counts():
	result = get_word_counts().most_common(5)
	expected = [('the', 12), ('of', 12), ('a', 9), ('and', 8), ('programming', 7)]


