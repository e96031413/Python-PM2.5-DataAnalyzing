import pandas as pd

df = pd.read_csv("https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv")
df1 = df.set_index(['county'])
i=df1.loc['高雄市']
print(i)