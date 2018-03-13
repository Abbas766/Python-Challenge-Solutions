#!/usr/bin/env python3

# Challenge 5 (peak.html) Solution

import pickle
from collections import Counter

f = open("banner.p","rb")
p = pickle.load(f)
arr=[]
for i in p:
	for j in i:
		print(j[0]*j[1],end="")
	print("\n")

		