# Challenge 8 ( integrity.html) solution

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup, Comment
import bz2

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
page = urlopen(url).read()
data = soup(page,'html.parser')

comments = data.find_all(string = lambda text:isinstance(text,Comment))
comment = comments[0].strip().split('\n')
cred = {} 


for i in comment:
	i=i.split(":")
	cred[i[0].strip()]=i[1].strip().strip("\'")
# k = bytes(cred["un"])
# print(k)

username = bz2.decompress(b'Abbas')

print(username)