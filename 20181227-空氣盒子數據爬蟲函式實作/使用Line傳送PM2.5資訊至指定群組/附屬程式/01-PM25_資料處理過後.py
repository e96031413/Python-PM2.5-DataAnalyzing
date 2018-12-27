import pandas as pd

df = pd.read_csv("https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv")
b=df.drop(labels=['DataCreationDate','ItemUnit'],axis='columns')
df1 = b.set_index(['county'])
i=df1.loc['高雄市']
print(i)