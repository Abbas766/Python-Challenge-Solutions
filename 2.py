#!/usr/bin/env python3

# Challenge 2 solution

####################################
# Dependencies:
#	1. Beautiful Soup
#	2. UrlLib
####################################	

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
from bs4 import Comment
from collections import Counter
from itertools import permutations

#url of the page
url = "http://www.pythonchallenge.com/pc/def/ocr.html"

# opening up connection and grabbing the page
uClient = uReq(url)
page_html= uClient.read()
uClient.close()

# parsing page for comments using beautiful soup
page_soup = Soup(page_html,'html.parser')
comments = page_soup.find_all(string = lambda text:isinstance(text,Comment))
random_text=""

# removing first line of comments 
comments = comments[1:]
for c in comments:
	random_text+=c
string = Counter(random_text)
rare_chars=""

# finding all rare (count == 1 ) characters into a string
for i in string.most_common():
	if(i[1]==1):
		rare_chars+=i[0]


# print all the permutations or rare characters found
lst = [ "".join(i) for i in permutations(rare_chars)]
print(lst)

# out of the printed permutations we found out a meaningful word ie. "equality"
newUrl = "http://www.pythonchallenge.com/pc/def/equality.html"
print(newUrl)





