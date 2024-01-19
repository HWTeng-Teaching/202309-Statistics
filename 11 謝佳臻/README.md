# 台灣GDP與房價的關聯性
- 作者：謝佳臻
- 創建日期：2023年11月4日
- 最後編輯日期：2024年1月19日

## Motivation
時任內政部部長的徐國勇及媒體報導都曾稱房地產是台灣經濟的火車頭，藉本次報告實際以資料觀察台灣GDP與房價的關聯性。

## Data

## Formulation
Assume the variable y is the growth rate of GDP, and the variable x is the growth rate of nationwide housing price index.
1. The probabilistic model is constructed as: y = ∝ + ßx + ε
2. Set up H0: ß = 0 versus H1: ß ≠ 0
3. The significance level is 0.05.
4. The test statistic tSTAT =  (b-0)/(MSE/Sxx) , which has a t distribution with df=39.
5. Rejection region {t: |t|>2.023} = {t>2.023 or t<-2.023}

## Analysis
H0  can not be rejected since the observed value of t doesn’t fall in the rejection region.
In addition, R square (SSR/(Total SS)) is close to 0, meaning the relationship between x and y is very week.

The model is not useful in the prediction of y.

## Conclusion
Based on the data, the growth rate of GDP is not linearly related to the growth rate of nationwide housing price index.
However, it is possible that one or more unknown variables that have not been included in the analysis may cause a linear relationship.
In addition, GDP growth rate has a wider fluctuation than housing price index on the seasonal basis.
Seasonality in GDP growth should also be taken into account.


## Link
Google Slides: https://docs.google.com/presentation/d/1yX2LlSQ_fD5FGOHGQzxgqQS-pqFW82edgj9wB0P1e8c/edit#slide=id.p
