import requests
from bs4 import BeautifulSoup
import os

os.environ["https_proxy"] = "http://nozaka.ryuji%40jp.fujitsu.com:5555555555@snd.proxy.nic.fujitsu.com:8080"

url = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
elems = soup.find_all(class_="ipQwMb ekueJc RD0gLb")
for e in elems:
  print(e.getText())