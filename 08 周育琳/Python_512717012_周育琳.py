import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager #因為想要印出中文字
import statsmodels.api as sm 
from statsmodels.formula.api import ols


# 利用 pands函數 讀取 CSV 檔案

df = pd.read_csv('data.csv')

#日期先備著用
df['Date'] = pd.to_datetime(df['Date'])


# 使用 '0056Price' 和 'Monitoring_Indicators' 欄位
# 計算 '0056Price' 的統計指標
# 使用 round 取小數點位數
average_0056_price = round(np.mean(df['0056Price']), 3)
median_0056_price = round(np.median(df['0056Price']), 3)
variance_0056_price = round(np.var(df['0056Price'], ddof=1), 3)
std_dev_0056_price = round(np.std(df['0056Price'], ddof=1), 3)
quartiles_0056_price = df['0056Price'].quantile([0.25, 0.5, 0.75]).round(3)
quartiles_0056_price.index = ['Q1=', 'Q2=', 'Q3=']

# 計算 'Monitoring_Indicators' 的統計指標
average_monitoring_indicators = round(np.mean(df['Monitoring_Indicators']), 3)
median_monitoring_indicators = round(np.median(df['Monitoring_Indicators']), 3)
variance_monitoring_indicators = round(np.var(df['Monitoring_Indicators'], ddof=1), 3)
std_dev_monitoring_indicators = round(np.std(df['Monitoring_Indicators'], ddof=1), 3)
quartiles_monitoring_indicators = df['Monitoring_Indicators'].quantile([0.25, 0.5, 0.75]).round(3)
quartiles_monitoring_indicators.index = ['Q1', 'Q2', 'Q3']


#計算簡單線性回歸 景氣訊號燈變動跟0056E股價的關係

X = df[['Monitoring_Indicators']] 
Y = df['0056Price']   

# 建立線性回歸模型
model = LinearRegression()
model.fit(X, Y)

# 使用模型進行預測
Y_pred = model.predict(X)

# 計算
mse =round( mean_squared_error(Y, Y_pred),3)
r2 = round(r2_score(Y, Y_pred),3)

# 列印結果
print("0056 價格指標 的統計指標:")
print("平均數:", average_0056_price)
print("中位數:", median_0056_price)
print("變異數:", variance_0056_price)
print("標準差:", std_dev_0056_price)
print("四分位數:\n", quartiles_0056_price)

print("\n 景氣訊號燈燈號的統計指標:")
print("平均數:", average_monitoring_indicators)
print("中位數:", median_monitoring_indicators)
print("變異數:", variance_monitoring_indicators)
print("標準差:", std_dev_monitoring_indicators)
print("四分位數:\n", quartiles_monitoring_indicators)

#列印簡單線性回歸結果

print("係數:", model.coef_)
print("截距:", model.intercept_)
print("均方誤差 (MSE):", mse)
print("R^2 分數:", r2)

# 繪製景氣訊號燈隨時間的變化
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Monitoring_Indicators'])
plt.title('TW_Monitoring_Indicators_2008 to 2022')
plt.xlabel('year')
plt.ylabel('Light')
plt.grid(True)
plt.show()

# 繪製0056股價隨時間的變化
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['0056Price'], color='red')
plt.title('0056pricetrend_2008 to 2022')
plt.xlabel('year')
plt.ylabel('0056Price')
plt.grid(True)
plt.show()

#繪製0056和景氣對策訊號燈 boxplot

df.boxplot(column=['0056Price'])
plt.title('Boxplot of 0056Price')
plt.show()


df.boxplot(column=['Monitoring_Indicators'])
plt.title('Boxplot of Monitoring Indicators')
plt.show()


# 繪製散布圖和回歸線

plt.figure(figsize=(10, 6))
plt.scatter(df['Monitoring_Indicators'], df['0056Price'])
plt.plot(df['Monitoring_Indicators'], Y_pred, label='regression line', color='red')
plt.title('Indicators & 0056 price regression analyze')
plt.xlabel('Indicators')
plt.ylabel('0056 price')
plt.legend()
plt.grid(True)
plt.show()


# 等待用戶輸入
input("按下 Enter 鍵退出...")
