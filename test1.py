# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:00:10 2024

@author: 包凯华
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 获取表格数据
table = soup.find('table', {'class':'dataTable'})
rows = table.find_all('str')

# 提取表头
header = [th.text for th in rows[0].find_all('th')]

# 提取数据
data = []
for row in rows[1:]:
    cols = row.find_all('td')
    data.append([col.text for col in cols])

# 转换为DataFrame
df = pd.DataFrame(data, columns=header)

# 筛选条件：Bond Type=Treasury Bond, Issue Year=2023
filtered_df = df[(df['Bond Type'] == 'Treasury Bond') & (df['Issue Date'].str.contains('2023'))]

# 保存为CSV文件
filtered_df.to_csv('treasury_bonds_2023.csv', index=False)