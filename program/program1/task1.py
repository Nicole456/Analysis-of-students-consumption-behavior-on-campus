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

任务 1.1 理解字段含义。探查数据质量并进行缺失值和异常值等
方面的必要处理。 

'''

# 导入数据
df1 = pd.read_csv('data1.csv', encoding='gbk')
df2 = pd.read_csv('data2.csv', encoding='gbk')
df3 = pd.read_csv('data3.csv', encoding='gbk')

# 数据信息总览
print('**************************************************')
print(df1.shape)
print('**************************************************')
print(df2.shape)
print('**************************************************')
print(df3.shape)
print('**************************************************')

print('未去重: ', df1.shape)
print('去重: ', df1.drop_duplicates().shape)

print('未去重: ', df2.shape)
print('去重: ', df2.drop_duplicates().shape)

print('未去重: ', df3.shape)
print('去重: ', df3.drop_duplicates().shape)


print('**************************************************')
print(df1.info())
print('**************************************************')
print(df2.info())
print('**************************************************')
print(df3.info())
print('**************************************************')


print('**************************************************')
print(df1.describe())
print('**************************************************')
print(df2.describe())
print('**************************************************')
print(df3.describe())
print('**************************************************')

'''

**************************************************
(4341, 5)
**************************************************
(519367, 14)
**************************************************
(43156, 6)
**************************************************


# 检查重复值

均无重复值


df1.describe().to_csv('data1_describe.csv')
df2.describe().to_csv('data2_describe.csv')
df3.describe().to_csv('data3_describe.csv')

'''
# 重新摆放列位置
columns = ['CardNo', 'Date', 'Money', 'FundMoney', 'Surplus', 'CardCount', 'Type', 'TermNo', 'OperNo',
           'Dept']
df2 = pd.DataFrame(df2, columns=columns)
#print(df2.head())

# 观察消费总额和消费次数之间的关系
#df2.to_csv('task1_1.csv')
#df_money_amount=df2.groupby('CardNo')['Money'].sum().sort_values(ascending=False).to_frame().reset_index()
#df_money_times=df2.groupby('CardNo')['CardCount'].max().sort_values(ascending=False).to_frame().reset_index()


#sns.regplot(x='Money',y='CardCount',data=df2)
#plt.show()


sns.distplot(df2['CardCount'],bins=100,color='r')
sns.kdeplot(df2['CardCount'],shade=True)
'''
通过 distplot 和 kdeplot 绘制柱状图观察 CardCount 特征的分布情况，属于长尾类型的分布，
这说明了有很多消费次数过多且超出正常范围。
也可能是年级较为高的学生
'''

plt.show()




