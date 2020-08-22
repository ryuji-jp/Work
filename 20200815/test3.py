import requests
from bs4 import BeautifulSoup
import os

os.environ["https_proxy"] = "http://nozaka.ryuji%40jp.fujitsu.com:5555555555@snd.proxy.nic.fujitsu.com:8080"

url = "https://www.pref.iwate.jp/kurashikankyou/iryou/covid19/1029635/index.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
#elems = soup.find_all(class_="w100")
table = soup.findAll("table", {"class":"w100"})[0]
rows = table.findAll("th")
rows2 = table.findAll("td")

#タイトル行の配列
arrs_th = [] 
#中身の配列
arrs_td = []
#タイトル行を中身の配列と同じ数にした配列
arrs_1 = []

#タイトル行取得
for r in rows:
  #print(r.getText())
  arrs = r.getText()
  arrs_th.append(arrs)

#中身取得
for r2 in rows2:
  #print(r2.getText())
  arrs = r2.getText()
  arrs_td.append(arrs)

#print(len(arrs_td))

#arrs_thをarrs_tdと同じ数にする
count1 = 0
count1 = len(arrs_td)/len(arrs_th)
count1 = int(count1)
#arrs_1はarrs_tdと同じ数
arrs_1 = (arrs_th * count1)
  
print(arrs_1)

i = 0
for i in range (len(arrs_td)):
  print(arrs_1[i] ,arrs_td[i])
  



