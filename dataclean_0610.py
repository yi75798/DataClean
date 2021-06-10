#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
資料清理程式
Created on Thu Jun 10 10:01:39 2021

@author: liang-yi
"""
### 0.載入套件
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

### 1.讀取原始資料
data = pd.read_csv("/Volumes/GoogleDrive/我的雲端硬碟/台大政研/2021程式設計/final_project/raw_data/tsai_0601.csv")
# drop掉空值
data = data.dropna(axis = 0)

### 2.篩選出2020/5/10後的資料
## 處理時間格式
# 手動處理個別資料檔在爬蟲當天24小時內的資料
# 蔡英文
data["Time"].iloc[0] = "2021年5月31日"
data["Time"].iloc[1] = "2021年5月31日"
data["Time"].iloc[2] = "2021年5月31日"

# 去除時間只留日期
for i in data["Time"].index:
    if "上午" in data["Time"].loc[i]:
        data["Time"].loc[i] = "2021年" + data["Time"].loc[i].split("上午")[0]
    if "下午" in data["Time"].loc[i]:
        data["Time"].loc[i] = "2021年" + data["Time"].loc[i].split("下午")[0]
    if "年" not in data["Time"].loc[i]:
        data["Time"].loc[i] = "2021年" + data["Time"].loc[i]

## 轉換時間格式
dateformat = "%Y年%m月%d日"
for i in data["Time"].index:
    data["Time"].loc[i] = datetime.strptime(data["Time"].loc[i], dateformat)
    
## 篩選
for i in data["Time"].index:
    if data["Time"].loc[i] < datetime(2020, 5, 10):
        data = data.drop(i)

## 轉換回字串形式日期
for i in data["Time"].index:
    data["Time"].loc[i] = datetime.strftime(data["Time"].loc[i], "%Y/%m/%d")

### 3.去除outlier
### Reaction
## 先畫圖
x = data["Time"]
y = data["Reaction"]
plt.title("before clean")
plt.scatter(x, y)
plt.show()

## 超過平均數正負2個標準差的就刪掉
mean_Reaction = data["Reaction"].mean()
sigma_Reaction = data["Reaction"].std()

c = 0
for i in data["Reaction"].index:
    if (data["Reaction"].loc[i] < (mean_Reaction - 2 * sigma_Reaction)) or\
        (data["Reaction"].loc[i] > (mean_Reaction + 2 * sigma_Reaction)):
        data = data.drop(i)
        c += 1
print(f"共刪除 {c} 筆")

## 再畫圖
x = data["Time"]
y = data["Reaction"]
plt.title("after clean")
plt.scatter(x, y)
plt.show()

## Comment
## 先畫圖
x = data["Time"]
y = data["Comment"]
plt.title("before clean")
plt.scatter(x, y)
plt.show()

## 超過平均數正負2個標準差的就刪掉
mean_Comment = data["Comment"].mean()
sigma_Comment = data["Comment"].std()

c = 0
for i in data["Comment"].index:
    if (data["Comment"].loc[i] < (mean_Comment - 2 * sigma_Comment)) or\
        (data["Comment"].loc[i] > (mean_Comment + 2 * sigma_Comment)):
        data = data.drop(i)
        c += 1
print(f"共刪除 {c} 筆")

## 再畫圖
x = data["Time"]
y = data["Comment"]
plt.title("after clean")
plt.scatter(x, y)
plt.show()

## Share
## 先畫圖
x = data["Time"]
y = data["Share"]
plt.title("before clean")
plt.scatter(x, y)
plt.show()

## 超過平均數正負2個標準差的就刪掉
mean_Share = data["Share"].mean()
sigma_Share = data["Share"].std()

c = 0
for i in data["Share"].index:
    if (data["Share"].loc[i] < (mean_Share - 2 * sigma_Share)) or\
        (data["Share"].loc[i] > (mean_Share + 2 * sigma_Share)):
        data = data.drop(i)
        c += 1
print(f"共刪除 {c} 筆")

## 再畫圖
x = data["Time"]
y = data["Share"]
plt.title("after clean")
plt.scatter(x, y)
plt.show()

### 4.輸出整理後的檔案
# 檔名記得改
data.to_csv(path_or_buf=u"/Volumes/GoogleDrive/我的雲端硬碟/台大政研/2021程式設計/final_project/cleaned_data/tsai_clean.csv", index=False, encoding="utf-8")
data.to_excel(u"/Volumes/GoogleDrive/我的雲端硬碟/台大政研/2021程式設計/final_project/cleaned_data/tsai_clean.xls", index=False, encoding="utf-8")



