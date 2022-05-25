import pytest

from text_analysis import WordInfo
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