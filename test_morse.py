import pytest
import morse 
import csv

@pytest.mark.morse
def test_encode():

	assert morse.encode("HEY YOU") == ".... . -.--    -.-- --- ..-"

	with open('data/test_cases_morse.csv', newline='') as csvfile:
	    reader = csv.reader(csvfile)
	    for row in reader:
	        assert morse.encode(row[0]) == row[1]

@pytest.mark.morse
def test_decode():
	assert morse.decode(".... . -.--    -.-- --- ..-") == "HEY YOU"
