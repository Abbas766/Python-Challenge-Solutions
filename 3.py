#!/usr/bin/env python3

# Challenge 3 solution
# One small letter, surrounded by  EXACTLY three big bodyguards on each of its sides.

####################################
# Dependencies:
#	1. Beautiful Soup
#	2. UrlLib
#	3. re
####################################	

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
from bs4 import Comment
import re

#url of the page
url = "http://www.pythonchallenge.com/pc/def/equality.html"

# opening up connection and grabbing the page
uClient = uReq(url)
page_html= uClient.read()
uClient.close()

# parsing page for comments using beautiful soup
page_soup = Soup(page_html,'html.parser')
comments = page_soup.find_all(string = lambda text:isinstance(text,Comment))
url = ""
# Parsing each line ofcomments and matching the regec for "aABCdEFGh"
# so that it matches those strings which have EXACTLY 3 Uppercase letter either side
for c in comments:
	string = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',c)
	for i in string:
		url+=i[4] 	# merging the smaller character from each match into a string to form the url clue.

print(url)

# Next level URL is : 
newUrl = "http://www.pythonchallenge.com/pc/def/"+url+".html"
print(newUrl)





