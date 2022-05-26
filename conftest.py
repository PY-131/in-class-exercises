import pytest
from text_analysis import WordInfo, TextAnalysis

@pytest.fixture
def word_info_obj():
   wd = WordInfo("apple")
   return wd

@pytest.fixture
def text_analysis_obj():
	file_ = "data/text1.txt"
	ta_obj = TextAnalysis(file_)
	return ta_obj