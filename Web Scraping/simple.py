# Web Scraping from a simple website

import requests
from bs4 import BeautifulSoup

response = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
content = response.content

parser = BeautifulSoup(content, 'html.parser')
head = parser.head
title = head.title

body = parser.body
p = body.p

print(title.text)
print(p.text)

# body = parser.find_all("body")
#
# p = body[0].find_all("p")
#
# # Get the text.
# print(p[0].text)
# head = parser.find_all("head")
# title = head[0].find_all("title")
# title_text = title[0].text



