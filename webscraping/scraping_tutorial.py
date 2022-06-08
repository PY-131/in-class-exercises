html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# print(f"the title of our web page is {soup.title}")
# print(f"A paragraph is {soup.p.get_text()}")

# for p in soup.find_all("a"):
# 	print(p.get_text())


# gets all the hrefs associated with anchors '<a>'
# for link in soup.find_all('a'):
#     print(link.get('href'))

# get parent element of all paragraphs <p>
for p in soup.find_all("p"):
	print(p.parent)
	# for child in p.children:
	# 	print(child)
	# print("-------------------")


