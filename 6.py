# Challenge 6(channel.html) Solution
# 1) Replace the url with .zip like http://www.pythonchallenge.com/pc/def/channel.zip
#	 and download the .zip file
# 2) use zipfile module to read files and comments
# It hints to start traversing from 90052.txt and says answer is inside zip

import os
import re 
import zipfile


file ="90052.txt"
comments= []
f = zipfile.ZipFile(os.getcwd()+"/channel.zip")
while file:
	
	text = f.read(file).decode("utf-8")
	comments.append(f.getinfo(file).comment.decode("utf-8"))

	r = re.findall("Next nothing is (\d+)",text)
	if r:
		file =r[0]+".txt"
		print(r[0])
	else:
		file = None 
		break
for i in comments:
	print(i,end="")