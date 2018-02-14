#!/usr/bin/env python3

# code to make a character map ( dictionary type object)
# charmap={	'm': 'o', 'v': 'x', 'c': 'e', 'p': 'r', 'z': 'b', 'd': 'f', 'f': 'h', 'r': 't', 'j':
#			'l', 'w': 'y', 'e': 'g', 'g': 'i', 'u': 'w', 'q': 's', 'n': 'p', 'l': 'n', 's': 'u', 'b': 'd',
# 			'i': 'k', 'k': 'm', 'a': 'c', 'y': 'a', 'o': 'q', 'x': 'z', 't': 'v', 'h': 'j'}
charmap={}
for i in range(97,121):
	charmap[chr(i)]=chr(i+2)
charmap['y']='a'
charmap['z']='b'

# strings to be translated
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url='map'

# translating the strings using maketrans()
newString = string.translate(str.maketrans(charmap))
newUrl = url.translate(str.maketrans(charmap))

print(newString)
print("http://www.pythonchallenge.com/pc/def/"+newUrl+".html")

# Alternative method (manual)
"""
string = list(string.split(" "))
newString=[]
for word in string:
	newWord=""
	for character in word:
 		if character.isalpha():
			if ord(character)<121:
				newWord+=chr(ord(character)+2)
			else:
 				newWord+=chr((ord(character)%121)+97)
 		else:
 			newWord+=character
newString.append(newWord)	
newString=" ".join(newString)		
"""



 



