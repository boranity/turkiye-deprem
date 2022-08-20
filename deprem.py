import requests
from bs4 import BeautifulSoup as bs4

r = requests.get("http://www.koeri.boun.edu.tr/scripts/lst0.asp")
soup = bs4(r.content, "html.parser")
pre = soup.find("pre")
text = pre.text 
list = text.split("\n")


print("\n".join(list[4:600]))
