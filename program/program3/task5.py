
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
任务 3.1 根据学生的整体校园消费数据，计算本月人均刷卡频次和人均消
费额，并选择 3 个专业，分析不同专业间不同性别学生群体的消费特点。
任务 3.2 根据学生的整体校园消费行为，选择合适的特征，构建聚类模型，
分析每一类学生群体的消费特点。
任务 3.3 通过对低消费学生群体的行为进行分析，探讨是否存在某些特征，
能为学校助学金评定提供参考。

'''

df=pd.read_csv('task1_2_1.csv')
df=df[df['Type']=='消费']
columns = ['CardNo','Sex','Major','Date','Money','Surplus','Type','CardCount','Type','Dept']
df = pd.DataFrame(df, columns=columns)


times=df.groupby('CardNo')['Money'].size().to_frame().apply(lambda x: x.tolist())
per_times=np.sum(times['Money'])/np.size(times)
#print("本月人均消费频次为："+np.str(per_times)+'次')

money=df.groupby('CardNo')['Money'].sum().to_frame().apply(lambda x: x.tolist())
per_times=np.sum(money['Money'])/np.size(money)
#print("本月人均消费额为："+np.str(per_times)+'元')
'''
本月人均消费频次为：72.74118014361537次
本月人均消费额为：288.7773899469248元
'''

'''
并选择 3 个专业，分析不同专业间不同性别学生群体的消费特点。
Money,times,'Dept'
消费金额，消费频次，消费地点，消费时间
18国际金融
18艺术设计
18计算机应用
'''
finance=df[df['Major']=='18国际金融']
art=df[df['Major']=='18艺术设计']
computer=df[df['Major']=='18计算机应用']
data=finance.append(art).append(computer)

'''
用户消费金额的分布图（二八法则）、用户消费次数的分布图
、用户累计消费金额的占比
'''

x=range(0,200,5)
finance_money=finance.groupby('Sex')['Money'].sum().to_frame().apply(lambda x: x.tolist())


g1=sns.FacetGrid(data,col='Major')
g1.map(sns.barplot,'Sex','Money')
g2=sns.FacetGrid(data,col='Major')
g2.map(sns.barplot,'Sex','Surplus')
g3=sns.FacetGrid(data,col='Major')
g3.map(sns.barplot,'Sex','CardCount')

plt.show()










