# 台灣GDP與房價的關聯性
- 作者：謝佳臻
- 創建日期：2023年11月4日
- 最後編輯日期：2024年1月19日

## Motivation
時任內政部部長的徐國勇及媒體報導都曾稱房地產是台灣經濟的火車頭，藉本次報告實際以資料觀察台灣GDP與房價的關聯性。

<img width="416" alt="圖片1" src="https://github.com/jnh14/2023-Fall-Stat/assets/149865884/e2f942aa-9e1c-4a82-8492-0a4bb2ff48fb">

## Data
![圖片2](https://github.com/jnh14/2023-Fall-Stat/assets/149865884/1898f55b-358d-48d6-b20c-38c28b5793e5)
Figure 1 shows the quarterly GDP from 102Q1 to 112Q2

![圖片3](https://github.com/jnh14/2023-Fall-Stat/assets/149865884/52783f07-38e0-4f30-a3d3-3faf39ee5110)
Figure 2 shows the quarterly housing price index from 102Q1 to 112Q2

![圖片4](https://github.com/jnh14/2023-Fall-Stat/assets/149865884/cc42f9f7-87c4-4fef-9f64-5e25a876bcac)
Figure 3 shows the growth rate of quarterly GDP and nationwide housing price index

![圖片5](https://github.com/jnh14/2023-Fall-Stat/assets/149865884/24a91aa4-940f-436d-b1ff-d7549332ad54)
Figure 4 shows the growth rate of quarterly GDP and nationwide housing price index

Based on the above graphs, it seems that no positive relationship is shown.

## Formulation
Assume the variable y is the growth rate of GDP, and the variable x is the growth rate of nationwide housing price index.
1. The probabilistic model is constructed as: y = ∝ + ßx + ε
2. Set up H<sub>0</sub>: ß = 0 versus H<sub>1</sub>: ß ≠ 0
3. The significance level is 0.05.
4. The test statistic t<sub>STAT</sub> =  $`(b-0)/\sqrt{MSE/Sxx}`$ , which has a t distribution with df=39.
5. Rejection region {t: |t|>2.023} = {t>2.023 or t<-2.023}

## Analysis
H<sub>0</sub> can not be rejected since the observed value of t doesn’t fall in the rejection region.
Besides, R square is close to 0, meaning the relationship between x and y is very week.

The model is not useful in the prediction of y.

## Conclusion
Based on the data, the growth rate of GDP is not linearly related to the growth rate of nationwide housing price index.

However, it is possible that one or more unknown variables that have not been included in the analysis may cause a linear relationship.

In addition, Figure 3 shows GDP growth rate has a wider fluctuation than housing price index on the seasonal basis.
Seasonality in GDP growth should also be taken into account.

## Link
Google Slides: https://docs.google.com/presentation/d/1yX2LlSQ_fD5FGOHGQzxgqQS-pqFW82edgj9wB0P1e8c/edit#slide=id.p
