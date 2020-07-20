import pandas
import pandas as pd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
'''
任务 3.3 通过对低消费学生群体的行为进行分析，探讨是否存在某些特征，
能为学校助学金评定提供参考。
'''

# 经过task3.2的分析得出type为2的学生为低消费学生群体，
# 故将他们的数据提取出来进行分析
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('task1_2_1.csv')
df = df[df['Type'] == '消费']
df2=pd.read_csv('task3_2.csv')
df2=df2.groupby(['CardNo'])['type'].mean().to_frame().apply(lambda x: x.tolist())


# 选择单次消费金额、存款金额、消费次数作为特征
columns = ['Sex', 'Major', 'CardNo', 'Money', 'Surplus', 'CardCount']

sex_major = pd.DataFrame(df, columns=['Sex', 'Major', 'CardNo'])
df = pd.DataFrame(df, columns=columns)
data1 = df.groupby(['CardNo'])['Money'].count().to_frame().apply(lambda x: x.tolist())
data2 = df.groupby(['CardNo'])['CardCount'].max().to_frame().apply(lambda x: x.tolist())
# 将学生的存款中的平均值，作为存款值的代表
data3 = df.groupby(['CardNo'])['Surplus'].mean().to_frame().apply(lambda x: x.tolist())
data = data1.join(data2).join(data3)
data = data.join(sex_major)
data = data[['Sex', 'Major', 'Money', 'CardCount', 'Surplus']]

print(data)


'''
data_ispoor=data[data['type']==2]
data_notpoor=data[data['type']!=2]


data_ispoor_count=data_ispoor.groupby(['Major'])['CardCount'].size().to_frame().apply(lambda x: x.tolist())
data_notpoor_count=data_notpoor.groupby(['Major'])['CardCount'].size().to_frame().apply(lambda x: x.tolist())
data_ispoor_count.plot.bar()
data_notpoor_count.plot.bar()
'''

'''
data_ispoor_count=data_ispoor.groupby(['Major'])['CardCount'].size().to_frame().apply(lambda x: x.tolist())
data_ispoor.plot.hist()
plt.xticks(data_ispoor_count['Major'])
plt.show()
print(data_ispoor)
train_data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar()
'''
#data_ispoor[['']]



