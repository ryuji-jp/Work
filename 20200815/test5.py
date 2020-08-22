import requests
from bs4 import BeautifulSoup
import os
import json


url = "https://www.pref.iwate.jp/kurashikankyou/iryou/covid19/1029635/index.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.findAll("table", {"class":"w100"})[0]
rows = table.findAll("th")
rows2 = table.findAll("td")

#タイトル行の配列
arrs_th = [] 
#中身の配列
arrs_td = []
#タイトル行を中身の配列と同じ数にした配列
arrs_1 = []
#タイトルと中身を連携させた配列
arrs_2 = []
#辞書型
dict_1 = {}



#タイトル行取得
for r in rows:
  #print(r.getText())
  arrs = r.getText()
  arrs_th.append(arrs)

#タイトルの数
count2 = len(arrs_th)

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
  
#print(arrs_1)


for i in range (len(arrs_td)):
  #print(arrs_1[i] ,arrs_td[i])
  
  arrs = arrs_1[i] ,arrs_td[i]
  arrs_2.append(arrs)
  dic = {}
  dic = {arrs_1[i],arrs_td[i]}
  #dict.update(dic)


dic = {}
x = 0
for i in  range (1,count1+1):
  for j in range (count2):
    
    dic[arrs_1[x]] = arrs_td[x]
    #dict_1[i] = {i}
    x = x + 1
    #dict_1=dict(dic)
    #dict_1[i].update(dic)
    
    #print(dic)
  dict_1[i]=dict(dic)

#print(dict_1)

#json_str = json.dumps(dict_1)
json_1 = open("test.json", "w") 
json.dump(dict_1, json_1,indent=2,ensure_ascii=False) 

