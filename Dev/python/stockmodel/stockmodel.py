#!/usr/bin/env python
# coding: utf-8

# In[3]:


#リストから銘柄を選択
import string
import json
import subprocess
import pandas as pd
from selenium import webdriver
import numpy as np
from matplotlib import pyplot as plt
import sys
from collections import defaultdict
from time import sleep
import time
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
#%matplotlib inline

#chromedriverは都度更新が必要なものになる。
 
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://google.com')

browser = webdriver.Chrome()
#executable_path='/path/to/driver/chromedriver'
#export PATH=$PATH:/path/to/driver/chrome-driver
    
columnNames=[]
ETFComparisonsTable=[]
for num in range(0,7):
    browser.get("https://kabuoji3.com/stock/")
    browser.implicitly_wait(3)
    stockSearch=browser.find_element_by_class_name("form_inputs")
    stockSearchForm=stockSearch.find_element_by_class_name("form_txt")
    stockSearchForm.send_keys("日経225")
    btnClick=browser.find_element_by_class_name("btn_submit")
    browser.implicitly_wait(25) #implicitly_wait
    btnClick.click()

    
    #choose a stock out of list
    stockClick=browser.find_elements_by_class_name("clickable")
    stockClick[num].find_element_by_tag_name("a").click()
    stockTable=browser.find_element_by_class_name("table_wrap")
    stockLine=stockTable.find_elements_by_tag_name("tr")
    #browser.implicitly_wait(10)
    #price scraping with calculation
    if len(stockLine)==302:
        ETFComparisons=[]
        for i in range(2,152):
            stockETFPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
            stockETFPriceBefore=stockLine[i].find_elements_by_tag_name("td")
            ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
            ETFComparisons.append(ETFComparison)

        stockETFPriceAfter=stockLine[151].find_elements_by_tag_name("td")
        stockETFPriceBefore=stockLine[153].find_elements_by_tag_name("td")
        ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
        ETFComparisons.append(ETFComparison)

        #browser.implicitly_wait(3)
        for i in range(154,302):
            stockETFPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
            stockETFPriceBefore=stockLine[i].find_elements_by_tag_name("td")
            ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
            ETFComparisons.append(ETFComparison)

        ETFComparisonsTable.append(ETFComparisons)

        #pick up title
        stockTitleBox=browser.find_element_by_class_name("base_box_ttl")
        stockTitle=stockTitleBox.find_element_by_class_name("jp").text
        columnNames.append(stockTitle)
#browser.implicitly_wait(10)
#making ETF table

ETFTable=pd.DataFrame(ETFComparisonsTable)
ETFTable=ETFTable.T
ETFTable.columns=columnNames
#checking ETF table
ETFTable.head()


# In[4]:


#date scraping
browser.get("https://kabuoji3.com/stock/{}/".format(1321))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
dates=[]
for i in range(1,152):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
for i in range(153,302):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
df_date=pd.DataFrame()
df_date["date"]=dates
df_date["year"]=df_date["date"].apply(lambda x:int(x.split("-")[0]))
df_date["month"]=df_date["date"].apply(lambda x:int(x.split("-")[1]))
df_date["day"]=df_date["date"].apply(lambda x:int(x.split("-")[2]))
df_date.head()


# In[5]:


#stock scraping (comparison with yesterday)
browser.get("https://kabuoji3.com/stock/{}/".format(1321))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
targetStockComparisons=[]
for i in range(2,152):
    targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
    targetStockPriceBefore=stockLine[i].find_elements_by_tag_name("td")
    targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
    targetStockComparisons.append(targetStockComparison)
targetStockPriceAfter=stockLine[151].find_elements_by_tag_name("td")
targetStockPriceBefore=stockLine[153].find_elements_by_tag_name("td")
targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
targetStockComparisons.append(targetStockComparison)
for i in range(154,302):
    targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
    targetStockPriceBefore=stockLine[i].find_elements_by_tag_name("td")
    targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
    targetStockComparisons.append(targetStockComparison)
df=pd.DataFrame(targetStockComparisons)
df.columns=["日経225連動型上場投資信託：前日比"]
df.head()


# In[7]:


#add table
stockPriceTable=pd.concat([df_date,ETFTable],axis=1)
stockPriceTable=pd.concat([stockPriceTable,df],axis=1)
stockPriceTable.head()


# In[6]:


#columnNames=[]
#ETFComparisonsTable=[]


# In[8]:


#prepare for making target values
df_next=df.copy()
df_next.columns=["日経225連動型上場投資信託：翌日比"]

#date scraping for target values
browser.get("https://kabuoji3.com/stock/{}/".format(1321))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
dates=[]
for i in range(2,152):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
for i in range(153,302):
    stockDate=stockLine[i].find_elements_by_tag_name("td")
    stockDate=stockDate[0].text
    dates.append(stockDate)
df_date2=pd.DataFrame()
df_date2["date"]=dates

#making target values table
df_next=pd.concat([df_date2,df_next],axis=1)
df_next.index=df_date2["date"]

#prepare for complete table
table=stockPriceTable[1:300].copy()
table.index=table["date"]

#making complete table
table["日経225連動型上場投資信託：翌日比"]=df_next["日経225連動型上場投資信託：翌日比"]
table.tail()


# In[9]:


table.to_csv("./stockPriceData.csv",index=False)


# In[10]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#%matplotlib inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from selenium import webdriver
import requests
import json

#reading csv file (*ETF=Exhange Traded Funds)
train=pd.read_csv("./stockPriceData.csv")
train=train.dropna()
train.head()


# In[11]:


features=['1329 iシェアーズ・コア 日経225ETF','1320 ダイワ 上場投信-日経225',
          '1346 MAXIS 日経225上場投信','1369 One ETF 日経225',
          '1578 上場インデックスファンド日経225(ミニ)'
          ,'日経225連動型上場投資信託：前日比']
#'2525 NZAM 上場投信 日経225'
x=train[features]
y=train["日経225連動型上場投資信託：翌日比"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.27)

#model making and prediction
model=RandomForestRegressor(n_estimators=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


#make result score and get accuracy score
testUpDown=[]
for test in y_test:
    if test>0:
        testUpDown.append(1)
    else:
        testUpDown.append(-1)
predUpDown=[]
for pred in y_pred:
    if pred>0:
        predUpDown.append(1)
    else:
        predUpDown.append(-1)
       
    
#print("確率："+str(metrics.accuracy_score(testUpDown,predUpDown)*100)+"%")

#feature evaluation and plots
#feature_imp = pd.Series(model.feature_importances_,index=features).sort_values(ascending=False)
#print(feature_imp)
#sns.barplot(x=feature_imp, y=feature_imp.index)
#plt.xlabel('Feature Importance Score')
#plt.ylabel('Features')
#plt.title("Visualizing Important Features")
#plt.figure(figsize=(30,50))
#plt.show()


########################################################################
browser=webdriver.Chrome()#'/Users/noss/Downloads/chromedriver'
columnNames=[]
ETFComparisonsTable=[]
ETFfeatures=['1329 iシェアーズ・コア 日経225ETF','1320 ダイワ 上場投信-日経225',
          '1321 日経225連動型上場投資信託','1346 MAXIS 日経225上場投信',
          '1369 One ETF 日経225','1578 上場インデックスファンド日経225(ミニ)',
          '2525 NZAM 上場投信 日経225']
for feature in ETFfeatures:
    feature=feature.split(" ")[0]

    browser.get("https://kabuoji3.com/stock/{}/".format(feature))
    stockTable=browser.find_element_by_class_name("table_wrap")
    stockLine=stockTable.find_elements_by_tag_name("tr")

    #price scraping with calculation
    if len(stockLine)==302:
        ETFComparisons=[]
        stockETFPriceAfter=stockLine[1].find_elements_by_tag_name("td")
        stockETFPriceBefore=stockLine[2].find_elements_by_tag_name("td")
        ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPriceBefore[6].text)
        ETFComparisons.append(ETFComparison)
        ETFComparisonsTable.append(ETFComparisons)

        #pick up title
        stockTitleBox=browser.find_element_by_class_name("base_box_ttl")
        stockTitle=stockTitleBox.find_element_by_class_name("jp").text
        columnNames.append(stockTitle)

#making ETF table
ETFTable=pd.DataFrame(ETFComparisonsTable)
ETFTable=ETFTable.T
ETFTable.columns=columnNames


#date scraping and stock scraping (comparison with yesterday)
browser.get("https://kabuoji3.com/stock/{}/".format(1321))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")

dates=[]
stockDate=stockLine[1].find_elements_by_tag_name("td")
stockDate=stockDate[0].text
dates.append(stockDate)

df_date=pd.DataFrame()
df_date["date"]=dates
df_date["year"]=df_date["date"].apply(lambda x:int(x.split("-")[0]))
df_date["month"]=df_date["date"].apply(lambda x:int(x.split("-")[1]))
df_date["day"]=df_date["date"].apply(lambda x:int(x.split("-")[2]))

targetStockComparisons=[]
targetStockPriceAfter=stockLine[1].find_elements_by_tag_name("td")
targetStockPriceBefore=stockLine[2].find_elements_by_tag_name("td")
targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
targetStockComparisons.append(targetStockComparison)

df=pd.DataFrame(targetStockComparisons)
df.columns=["日経225連動型上場投資信託：前日比"]

#add table
stockPriceTable=pd.concat([df_date,ETFTable],axis=1)
stockPriceTable=pd.concat([stockPriceTable,df],axis=1)


#ready for future price prediction
valueX=stockPriceTable[features]
pred=model.predict(valueX)
print(pred)
#make result score and get accuracy score
predPriceUpDown="?"
if pred>0:
    predPriceUpDown="上昇"
else:
    predPriceUpDown="下落"

#telling result
resultNotification="「日経225連動型上場投資信託:\n"+stockDate+"現時点での予測値は"+str(float(targetStockPriceAfter[6].text)+float(pred))+"円。\nよって価格は"+predPriceUpDown+"見込みです。"
#print(resultNotification)
browser.quit()

#SlackBot
slackURL="https://hooks.slack.com/services/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"

def send_slack(content):
    payload={
        "text":content,
        "username":"PythonStockForecast",
        "icon_emoji":":ghost:"
    }
    data=json.dumps(payload)
    requests.post(slackURL,data)
send_slack(resultNotification)

