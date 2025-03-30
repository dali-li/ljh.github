import pandas as pd
import matplotlib.pyplot as plt
import os

# 确保数据文件存在，不存在则创建
file_path = 'data.xlsx'
if not os.path.exists(file_path):
    data = {
        '日期': ['2018/1/1', '2018/1/2', '2018/1/3', '2018/1/4', '2018/1/5', 
               '2018/1/6', '2018/1/7', '2018/1/8', '2018/1/9', '2018/1/10',
               '2018/1/11', '2018/1/12', '2018/1/13', '2018/1/14', '2018/1/15'],
        '猪肉价格': [11, 12, 11.5, 12, 12, 11.2, 13, 12.6, 13.5, 13.9, 13.8, 14, 13.5, 14.5, 14.8],
        '牛肉价格': [38, 39, 41.3, 40, 43, 44, 47, 43, 42.3, 42, 43.1, 42, 39, 38, 37.5]
    }
    df_initial = pd.DataFrame(data)
    df_initial.to_excel(file_path, index=False)

# 读取数据并处理日期格式
df = pd.read_excel(file_path)
df['日期'] = pd.to_datetime(df['日期'])

# 提取前10天数据
df_first10 = df.head(10)

# 绘制前10天猪肉价格走势
plt.figure(figsize=(10, 5))
plt.plot(df_first10['日期'], df_first10['猪肉价格'], marker='o', color='green')
plt.title('前10天猪肉价格走势')
plt.xlabel('日期')
plt.ylabel('价格（元）')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制前10天牛肉价格走势
plt.figure(figsize=(10, 5))
plt.plot(df_first10['日期'], df_first10['牛肉价格'], marker='o', color='red')
plt.title('前10天牛肉价格走势')
plt.xlabel('日期')
plt.ylabel('价格（元）')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制2x1子图显示全半月价格
plt.figure(figsize=(10, 8))

# 猪肉价格子图
plt.subplot(2, 1, 1)
plt.plot(df['日期'], df['猪肉价格'], marker='o', color='green')
plt.title('2018年1月前半月猪肉价格走势')
plt.xlabel('日期')
plt.ylabel('价格（元）')
plt.grid(True)
plt.xticks(rotation=45)

# 牛肉价格子图
plt.subplot(2, 1, 2)
plt.plot(df['日期'], df['牛肉价格'], marker='o', color='red')
plt.title('2018年1月前半月牛肉价格走势')
plt.xlabel('日期')
plt.ylabel('价格（元）')
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()