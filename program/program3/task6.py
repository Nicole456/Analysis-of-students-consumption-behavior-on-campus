import matplotlib
import pandas
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
sns.set_style({'font.sans-serif': ['simhei', 'Arial']})
'''
任务 3.2 根据学生的整体校园消费行为，选择合适的特征，构建聚类模型，
分析每一类学生群体的消费特点。
'''

df = pd.read_csv('task1_2_1.csv')
df = df[df['Type'] == '消费']

# 选择单次消费金额、存款金额、消费次数作为特征
columns = ['CardNo', 'Money', 'Surplus', 'CardCount']
df = pd.DataFrame(df, columns=columns)

data1 = df.groupby(['CardNo'])['Money'].count().to_frame().apply(lambda x: x.tolist())
data2 = df.groupby(['CardNo'])['CardCount'].max().to_frame().apply(lambda x: x.tolist())

# 将学生的存款中的平均值，作为存款值的代表
data3 = df.groupby(['CardNo'])['Surplus'].mean().to_frame().apply(lambda x: x.tolist())

data = data1.join(data2).join(data3)

k = 4  # 聚类的类别
iteration = 500  # 聚类的最大循环次数

data_zs = 1.0 * (data - data.mean()) / data.std()  # 数据标准化
# print(data_zs)

from sklearn.cluster import KMeans

model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)  # 分为k类，并发数4
model.fit(data_zs)  # 开始聚类

# 简单打印结果
r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
print(r)
'''
      Money  CardCount   Surplus  类别数目
0 -0.702351  -0.692987 -0.463079  1580
1  0.102485   0.077026  1.697912   475
2  0.924246   0.921892 -0.065195  1148

'''

data_zs['type']=model.predict(data_zs)
data['type']=data_zs['type']

# 通过聚类类别对各属性特征进行分类
data_group=data.groupby(['type'])

# 对dmean数据框进行添加数据执行FOR循环,这是两层循环

dMean = pandas.DataFrame()  # 初始化
plt.figure(figsize=(16,16)) # 条形图大小
j=-1
for g in data_group.groups:
    rMean = data_group.get_group(g).mean()
    rMean['分类'] = g;
    rMean['总计'] = data_group.get_group(g).size / 7
    dMean = dMean.append(rMean, ignore_index=True)
    # 通过直方图查看各个类别对应所有属性之间的差异

    subData = data_group.get_group(g)
    i = 0
    j = j + 1

    for column in ['Money', 'Surplus', 'CardCount']:
        i=i+1
        p = plt.subplot(1, 3, i)
        p.set_title(column)

        plt.hist(subData[column],label=j,alpha=0.6)

        plt.tight_layout()  # 调整子图间距

plt.legend()
plt.show()

data.to_csv('task3_2.csv')
