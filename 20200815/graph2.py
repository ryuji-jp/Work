import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import requests
from bs4 import BeautifulSoup
import os
import json
import re


url = "https://www.pref.iwate.jp/kurashikankyou/iryou/covid19/index.html"
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
#中身全体を配列
arrs_td_list2 = []
#th配列の長さ
arrs_th_list3 = []

aomori = []
iwate = []
miyagi = []
akita = []
yamagata = []
hukushima = []

#タイトル行取得
for r in rows:
  #print(r.getText())
  arrs = r.getText()
  
  if arrs == "\n青森県\n":
    break
  
  arrs_th.append(arrs)

#print(arrs_th)
#配列をきれいに
arrs_th_list = [s.replace('\n', '') for s in arrs_th]

for z in range(1,len(arrs_th_list)):
  arrs_th_list3.append(arrs_th_list[z])
  
#print(arrs_th_list3)

#th配列の長さ
th_count = len(arrs_th_list3)

#print(arrs_th_list)

#中身取得
for r2 in rows2:
  #print(r2.getText())
  arrs = r2.getText()
  arrs_td.append(arrs)

#print(arrs_td)
arrs_td_list = [s.replace('\n', '') for s in arrs_td]
#print(arrs_td_list)

for i in range(len(arrs_td_list)):
  s = arrs_td_list[i] 
  s_list = []
  s_list = re.sub('（[0-9]*）', '', s)
  arrs_td_list2.append(s_list) 
  #print(re.sub('（[0-9]*）', '', s))

#print(th_count)

for j in range(len(arrs_td_list)):
  if j < th_count :
    aomori.append(arrs_td_list2[j])

  elif j < th_count*2:
    iwate.append(arrs_td_list2[j]) 
  
  elif j < th_count*3:
    miyagi.append(arrs_td_list2[j]) 

  elif j < th_count*4:
    akita.append(arrs_td_list2[j]) 

  elif j < th_count*5:
    yamagata.append(arrs_td_list2[j]) 

  elif j < th_count*6:
    hukushima.append(arrs_td_list2[j]) 

#arrs_td_list2 = [re.sub(r'（）', '') for s in arrs_td_list]
#print(arrs_td_list2)
#print(aomori)
#print(iwate)
#print(miyagi)
#print(akita)
#print(yamagata)
#print(hukushima)


plt.plot(arrs_th_list3, iwate, color = 'blue', marker = 'o',label = "岩手") 
plt.plot(arrs_th_list3, aomori, color = 'red', marker = 'o',label = "青森")
plt.plot(arrs_th_list3, miyagi, color = 'green', marker = 'o',label = "宮城")

plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10)
plt.show()

