import pandas as pd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})

'''
任务 2.2 通过食堂刷卡记录，分别绘制工作日和非工作日食堂就餐时间曲
线图，分析食堂早中晚餐的就餐峰值
'''

df=pd.read_csv('task1_1.csv')

df['datetime']=pd.to_datetime(df['Date'],format='%Y/%m/%d %H:%M',errors='coerce')

df['dayofweek']=df['datetime'].dt.dayofweek
df['hour']=df['datetime'].dt.hour
df.drop(['datetime'],axis=1,inplace=True)

weekend=df[(df['dayofweek']==0)|(df['dayofweek']==6)]
weekday=df[(df['dayofweek']!=0)&(df['dayofweek']!=6)]


weekend=weekend.groupby('hour')['Money'].size().to_frame().apply(lambda x: x.tolist())
weekday=weekday.groupby('hour')['Money'].size().to_frame().apply(lambda x: x.tolist())
weekday.rename(columns={'Money':'times'},inplace=True)
weekend.rename(columns={'Money':'times'},inplace=True)



x = range(1,25,1)

plt.figure(figsize=(15,5))
plt.subplot(121)
plt.title('非工作日食堂就餐时间图')
plt.xticks(x)

weekend['times'].plot()
plt.subplot(122)
plt.title('工作日食堂就餐时间图')
plt.xticks(x)

weekday['times'].plot()


plt.show()





