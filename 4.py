#!/usr/bin/env python3

# Challenge 4 (linkedlist.php) Solution
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
client = urlopen(url)
data = soup(client,'html.parser')
link = data.a.get('href')
r = re.match('linkedlist\.php\?nothing=(\d+)',link)
nothing = r.group(1)
i=0
while i<400 or nothing!=None:
	url ="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+(nothing)
	client = urlopen(url)
	data = soup(client,'html.parser')
	text = data.text
	
	r = re.findall("and the next nothing is ([0-9]+)",text)
	if len(r)!= 0:
		nothing = r[0]
		print(nothing)
	elif re.match('Yes. Divide by two and keep going.',text):
		nothing = str(int(nothing)//2)
		print(nothing)
	else:
		print("New link: %s"%text)
		break
	i+=1



