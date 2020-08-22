import requests
from bs4 import BeautifulSoup
import os

os.environ["https_proxy"] = "http://nozaka.ryuji%40jp.fujitsu.com:5555555555@snd.proxy.nic.fujitsu.com:8080"

url = "https://www.pref.iwate.jp/kurashikankyou/iryou/covid19/1029635/index.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
elems = soup.find_all(class_="w100")

for e in elems:
  print(e.getText())