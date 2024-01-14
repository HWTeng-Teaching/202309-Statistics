# 股票市場-價與量的關係 (以0050成份股為例)

- 作者：512717009 范艾雯 / 512717024 江文煌 / Advisor 鄧惠文
- Github創建日期：2023年11月04日
- 專案完成日期：2023年11月25日
- Github最後編輯日期：2024年01月14日
 
Data link: https://drive.google.com/drive/folders/1iiufHPsDV5xPbTk0ZkSwnve9N2f7uYFm?usp=sharing

Project ppt link: https://drive.google.com/file/d/1VOX8BKsV993_yxkrErzVrNKbnF1KAQnV/view?usp=sharing
Python code link: https://drive.google.com/drive/folders/1AS1_2CAsnAvm7qbc5I6CRb3ZprNco843?usp=sharing

影片連結: https://youtu.be/qlo21SVhb5E

### ---------------------------------------------------------------------------------------
![](https://drive.usercontent.google.com/download?id=1gNC7d9x9R_xYm5aopOpOpNiAhSF89B9J&export=download&authuser=0&confirm=t&uuid=cb6f46df-30ae-4845-92ff-7f1a57decd3a&at=APZUnTX7VMzajaucMwvAXYJof7jh:1703471428483)

## Gather Information：
目前以元大台灣50(0050)成份股市值權重分布排名在前、中、後各3家，資料搜集期間為2022.11.10~2023.11.09近一年間的成交量與價之數值，初步分析各股間成交量與成交價的變化關係，並結合統計學Chapter 1之課程內容，劃出時間序列圖（Line charts）。

# 資料收集
![](https://drive.usercontent.google.com/download?id=1hh38bYzkU5klEkvzQbseGmVTKwkzZufe&export=download&authuser=0&confirm=t&uuid=4b1ba333-86c9-429f-8a24-8741680fc3fd&at=APZUnTWJiAF9VSEcYBTRjGonMIf2:1702045588861)

. 

# 資料視覺化 Exploratory data analysis 
![](https://drive.usercontent.google.com/download?id=1ZRCwuwX-FVnSKKAektZXAe5MmEW3yHjo&export=download&authuser=0&confirm=t&uuid=64ad2dd0-bd78-4d68-8d59-ddb3915dc409&at=APZUnTWmhY1zsQz3dpM3ab4wjN9h:1703471450021)  

.

# 研究方法
### 量比價先行
### 以ㄧ檔0050成份股為研究標的，取一整個年度的交易資料。分析是否當成交量有相當變化幅度後，在某個時間點，會有相當幅度的價格變化幅度，而且此現象會存在非常高的出現機率。                    

.

# 研究變數定義與目標
###   
### 研究標的: 2330.tw 台積電
資料區間(一年)：2022.01.03~2022.12.30(交易日)
成交量變化幅度: 50% up
價格變化幅度: 2% up
出現機率(重現率): 90% up 
###   
### ※當成交量有50%的變動時，x天後的股價變動率達到2%以上的機率超過90%

.

# 資料視覺化 Exploratory data analysis 2nd 

![](https://drive.usercontent.google.com/download?id=12vumd432NnvzfiUb-fl3b0P10pOilYpb&export=download&authuser=0&confirm=t&uuid=120808f9-0d56-42f9-9e52-fb647d80faba&at=APZUnTVwC5vBy9t7tl8YScZZ7-F7:1703475897182)

 .
 
# 決定xDay
 
![](https://drive.usercontent.google.com/download?id=142kNF1WwWzqjwK_P9xdNRqj6fYe0iseS&export=download&authuser=0&confirm=t&uuid=b0d2bc05-c979-4c50-a1c2-7a8dcce21ebf&at=APZUnTXKpFWgbUFf_naXpbKGPY5E:1702050104904)

![](https://drive.usercontent.google.com/download?id=1wAAYuNrnWqidIDVUfAhuchw1TuXY0R5L&export=download&authuser=0&confirm=t&uuid=5bcf70fc-76c0-4747-a2d8-bf85ee1402bf&at=APZUnTW1VbE7AHQ8qVO8NpY1zSVK:1702048142367)

.

# xDay =Day+14

![](https://drive.usercontent.google.com/download?id=1OaY303nnVpREzk1jO0t0q0Dor1iJbDG6&export=download&authuser=0&confirm=t&uuid=46113a0e-8992-4bcb-97c8-2d792db4ce72&at=APZUnTVl0OaqDWWPwyB9RRVX65nx:1702048171951)

.

# 驗證步驟
  
![](https://drive.usercontent.google.com/download?id=15Z5a8dSE1mVVP1hhvn8jskwpbFXNx1lQ&export=download&authuser=0&confirm=t&uuid=55f114af-acf3-4aeb-a4b1-f86a24e14a88&at=APZUnTX2D5CTomOnlFCOlKup6IQu:1702050301858)

# 
 
![](https://drive.usercontent.google.com/download?id=1ROJUNP7oWbwOcYK32G8xTYjfPZQMqmhW&export=download&authuser=0&confirm=t&uuid=dc20e272-027c-43d2-b172-97ac48d2c743&at=APZUnTUFSnwS0rGEPdVeNlCIeApy:1703471457960)

 .
 
# 進階研究
 
![](https://drive.usercontent.google.com/download?id=1-oBnV0GNSWdQZpOew1TcPlAW7Od2IZNV&export=download&authuser=0&confirm=t&uuid=c5b7898d-c3d9-4854-97d6-bc91e2be87fa&at=APZUnTWnRgC98z0OQGbh68io0-85:1702050308949)
###   
![](https://drive.usercontent.google.com/download?id=1Xd_SHiyePFkeVmOQwTuziHoYCccXRQQP&export=download&authuser=0&confirm=t&uuid=0882711d-c83c-4347-a302-2f2a53be044a&at=APZUnTXIsmDeRMvh9Z8M4Zxpxz7V:1703471466203)  

.

# 未來研究方向
### 1.假設檢定給定條件不同，結果會有所差異，可做後續相關研究。
### 2.本案以2330成份股為例，後續可對其他股票做相同性研究分析。
### 3.透過本案統計分析結果，將應用於生活投資策略上，並可匯集同好，開發相關程式模組化，成立投資公司共同創業發展。

  .
  
# Search @ Youtube ~

![](https://drive.usercontent.google.com/download?id=18KbToKD1FWaTHlOtRFkfKIROQAceDFCc&export=download&authuser=0&confirm=t&uuid=51f2c32f-b8b4-4464-af00-31799273c47d&at=APZUnTWgb1VcoPlb3BAj-qVcBRiO:1703471478459)
##  附件
![image]05 范艾雯/DATAsFiles/Photos/01.jpg
![image](https://github.com/evan7352/2023-Fall-Stat/blob/main/05%20%E8%8C%83%E8%89%BE%E9%9B%AF/26.jpg)
![image](https://github.com/evan7352/2023-Fall-Stat/blob/main/05%20%E8%8C%83%E8%89%BE%E9%9B%AF/27.jpg)
![image](https://github.com/evan7352/2023-Fall-Stat/blob/main/05%20%E8%8C%83%E8%89%BE%E9%9B%AF/28.jpg)
