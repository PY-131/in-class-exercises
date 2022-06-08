from bs4 import BeautifulSoup
import requests as rqs
from pprint import pprint as pp


def scrape_quotes(URL = "https://quotes.toscrape.com/"):

	res_dict= dict()
	res_dict['quotes'] = []


	try:
		res = rqs.get(URL)
	except Exception as e:
		raise e

	soup = BeautifulSoup(res.content, 'html.parser')
	for div in soup.find_all("div", class_="quote"):
		res_dict['quotes'].append(__extract_data(div))
	return res_dict

def scrape_random_quote(URL = "https://quotes.toscrape.com/random"):


	try:
		res = rqs.get(URL)
	except Exception as e:
		raise e

	soup = BeautifulSoup(res.content, 'html.parser')
	
	return __extract_data(soup)

def __extract_data(soup):

	res_dict= dict()
	res_dict['quote'] = soup.find("span", class_="text").get_text()
	res_dict['author_name'] = soup.find("small", class_="author").get_text()
	res_dict['tags'] = __extract_tags(soup)
	return res_dict

def __extract_tags(elem):

	div_tag = elem.find("div", class_="tags")
	return [tag.text for tag in div_tag.find_all("a", class_="tag")]


if __name__ == '__main__':
	#print(scrape_random_quote()) 
	pp(scrape_quotes())