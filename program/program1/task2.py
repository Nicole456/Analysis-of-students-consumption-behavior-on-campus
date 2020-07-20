import pandas as pd
'''
任务 1.2 将 data1.csv 中的学生个人信息与 data2.csv 中的消费记录建立
关联，处理结果保存为“task1_2_1.csv”；将 data1.csv 中的学生个人信息与
data3.csv 中的门禁进出记录建立关联，处理结果保存为“task1_2_2.csv”。

'''
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# 导入数据
df1 = pd.read_csv('data1.csv', encoding='gbk')
df2 = pd.read_csv('data2.csv', encoding='gbk')
df3 = pd.read_csv('data3.csv', encoding='gbk')

data1_2=df1.merge(df2,left_on='CardNo',right_on='CardNo')
data1_2.rename(columns={"Index_x": "Stu_Index"}, inplace=True)
data1_2.rename(columns={"Index_y": "Con_Index"}, inplace=True)
#print(data1_2.head())

data1_3=df1.merge(df3,left_on='AccessCardNo',right_on='AccessCardNo')
data1_3.rename(columns={"Index_x": "Stu_Index"}, inplace=True)
data1_3.rename(columns={"Index_y": "Acc_Index"}, inplace=True)
#print(data1_3.head())

data1_2.to_csv('task1_2_1.csv')
data1_3.to_csv('task1_2_2.csv')
