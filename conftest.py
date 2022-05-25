import pytest
from text_analysis import WordInfo

@pytest.fixture
def word_info_obj():
   wd = WordInfo("apple")
   return wd