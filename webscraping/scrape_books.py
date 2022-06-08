from bs4 import BeautifulSoup
import requests as rqs
from pprint import pprint as pp
import json
import os

BASE_URL = "https://books.toscrape.com/catalogue/"

def write_to_json(results):

    
	with open("books.json", "w") as outfile:
	    json.dump(results, outfile)


def scrape_books():
	""" 
	scrapes books info
	""" 

	results = []
	CURR_URL = "page-1.html"
	CURRENT_PAGE = 1

	while True: 

		try:
			res = rqs.get(os.path.join(BASE_URL, CURR_URL))
		except Exception as e:
			raise e

		soup = BeautifulSoup(res.content, 'html.parser')
		for article in soup.find_all("article",class_="product_pod"):
			entry = dict()
			entry['title'] = article.h3.a["title"]
			entry['img_src'] = article.find("img").get("src")
			entry['price'] = article.find("p", {"class": "price_color"}).get_text().strip()
			entry['in_stock'] = article.find("p", {"class": "instock availability"}).get_text().strip().lower()
			entry["rating"] = article.p["class"][1].lower()
			results.append(entry)

		print(f"Finished scraping page {CURRENT_PAGE}")
		CURR = soup.find("li", {"class":"next"})

		# if the URL is not found, stop scraping
		if not CURR:
			break 
		else:
			CURR_URL = CURR.a["href"] 
		CURRENT_PAGE += 1

	return results

if __name__ == '__main__':
	results = scrape_books()
	write_to_json(results)



