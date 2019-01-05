# -*- coding: UTF-8 -*-
import requests      # 匯入 requests 套件
import pandas as pd

df = pd.read_csv("https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv")
b=df.drop(labels=['DataCreationDate','ItemUnit'],axis='columns')
df1 = b.set_index(['county'])
i=df1.loc['高雄市']
print(i)

def send_ifttt(v1):   # 定義函式來向 IFTTT 發送 HTTP 要求
    url = ('https://maker.ifttt.com/trigger/PM2.5_Crawler/with/' +
          'key/OCLxwpzP2IgEnJ7pYrYbD' +
          '?value1='+str(v1))
    r = requests.get(url)      # 送出 HTTP GET 並取得網站的回應資料
    if r.text[:5] == 'Congr':  # 回應的文字若以 Congr 開頭就表示成功了
        print('已傳送 (' +str(v1)+') 到 Line')
    return r.text

ret = send_ifttt(i)  #傳送 HTTP 請求到 IFTTT
print('IFTTT 的回應訊息：',ret)     # 輸出 IFTTT 回應的文字


