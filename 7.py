# Challege 7 (hockey.html) Solution

# In the previous solution graphic see the letters of the design where letters join to form word "HOCKEY"
# the words are "OXYGEN" and it's in the air.


from PIL import Image
from io import BytesIO
import requests

# get oxygen.png 
img  = Image.open(BytesIO(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content))

# extract the grey scale row from image
row = [img.getpixel((j,(img.height/2))) for j in range(img.width)]
# remove duplicates by manual observing as they are at distance of 7 pixels
row = row[::7]

ords = [r for r,g,b,a in row if r==g==b]
clue = "".join([chr(i) for i in ords])
print(clue)
# from clue 
nums= [105,110,116,101,103,114,105,116,121]
print("".join(map(chr,nums)))