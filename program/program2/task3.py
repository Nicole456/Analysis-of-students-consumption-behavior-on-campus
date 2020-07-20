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
任务 2 食堂就餐行为分析
任务 2.1 绘制各食堂就餐人次的占比饼图，分析学生早中晚餐的就餐地点
是否有显著差别，
'''
df=pd.read_csv('task1_1.csv')


df['datetime']=pd.to_datetime(df['Date'],format='%Y/%m/%d %H:%M',errors='coerce')
df['hour']=df['datetime'].dt.hour
df.drop(['datetime'],axis=1,inplace=True)

pattern='食堂'
df=df[df['Dept'].str.contains('食堂')]

morning=df[(df['hour']>=3)&(df['hour']<=10)]
noon=df[(df['hour']>10)&(df['hour']<=14)]
night=df[(df['hour']>15)&(df['hour']<=22)]


place_money=df.groupby(['Dept'])['Money'].size().sort_values(ascending=False).to_frame().apply(lambda x: x.tolist())
place_money.rename(columns={'Money':'times'},inplace=True)

morning_place_money=morning.groupby(['Dept'])['Money'].size().sort_values(ascending=False).to_frame().apply(lambda x: x.tolist())
morning_place_money.rename(columns={'Money':'times'},inplace=True)

noon_place_money=noon.groupby(['Dept'])['Money'].size().sort_values(ascending=False).to_frame().apply(lambda x: x.tolist())
noon_place_money.rename(columns={'Money':'times'},inplace=True)

night_place_money=night.groupby(['Dept'])['Money'].size().sort_values(ascending=False).to_frame().apply(lambda x: x.tolist())
night_place_money.rename(columns={'Money':'times'},inplace=True)
'''
place_money['times'].plot.pie(autopct = '%1.2f%%')

plt.figure(1)
plt.title('各食堂就餐人次的占比图')
plt.show()
'''

plt.figure(figsize=(15,5))
plt.subplot(131)
plt.title('早餐各食堂就餐人次的占比图')
morning_place_money['times'].plot.pie(autopct = '%1.2f%%')
plt.subplot(132)
plt.title('午餐各食堂就餐人次的占比图')
noon_place_money['times'].plot.pie(autopct = '%1.2f%%')
plt.subplot(133)
plt.title('晚餐各食堂就餐人次的占比图')
night_place_money['times'].plot.pie(autopct = '%1.2f%%')
plt.show()




'''
#ax1 = fig.add_subplot(2,2,1)  # 创建一个图表，该图在2行2列的子图中的第一个位置，即一行左图
plt.figure(1)
Jan['销售金额'].plot.pie(autopct = '%1.2f%%')
plt.title('一月份各大类商品销售金额的占比图')
plt.figure(2)
Feb['销售金额'].plot.pie(autopct = '%1.2f%%')
plt.title('二月份各大类商品销售金额的占比图')
plt.figure(3)
Mar['销售金额'].plot.pie(autopct = '%1.2f%%')
plt.title('三月份各大类商品销售金额的占比图')
plt.figure(4)
Apr['销售金额'].plot.pie(autopct = '%1.2f%%')
plt.title('四月份各大类商品销售金额的占比图')
plt.show()

'''

#print(df.head())

#df.to_csv('task3_1.csv')
#place_times=df.groupby('Dept')['Money'].sum().sort_values(ascending=False).to_frame().reset_index()









