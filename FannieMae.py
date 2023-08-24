# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:38:33 2023

@author: Faisal
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import glob

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
os.chdir("C:/Users/Faisal/Downloads/FannieMaeMortData/")
cwd = os.getcwd()
print("New working directory: {0}".format(cwd))

importfilelist = ["2022Q1", "2022Q2", "2022Q3", "2022Q4", "2023Q1"]

#The dictionary for the what each of the 108 columns are can be found at https://capitalmarkets.fanniemae.com/media/6931/display. 
#There is not enough memory to load all the columns at the same time or to load all the quarters."
#Take the 'Field Position' and subtract 1 to figure out the column names because indexing starts at 0."

colnames = [1,8,9,11,13,16,17,20,21,22,23,25,30,31,32,34,35,36,39,40]
headings = ["loanid","currint","origUPB","curractUPB","OrigDate","MTLM","MTM","CLTV","Numborr","DTI", "BorrCRS","FTHBI", "State", "MSA", "ZipShort", "ARMorFIX", "PPI", "IntONLY", "CurrDelinq", "PayHist"] 
#fanniemae = importfilelist
#fanniemae_2022Q1 = pd.read_csv('2022Q1.csv',sep='|')
#fanniemae_2022Q2 = pd.read_csv('2022Q1.csv',sep='|')
#fanniemae_2022Q3 = pd.read_csv('2022Q1.csv',sep='|')
#fanniemae_2022Q4 = pd.read_csv('2022Q1.csv',sep='|')
fanniemae_2023Q1 = pd.read_csv('2022Q1.csv',sep='|', usecols=colnames, names=headings)
fanniemae_2023Q1.apply(lambda x: x.isnull().sum(), axis=0)

fanniemae_2023Q1.groupby(['FTHBI','State'])['currint','BorrCRS','DTI'].mean()
fanniemae_2023Q1.groupby(['FTHBI','State'])['loanid'].count()

#There are a total of 889 regions by 3 digit zip-codes.
#len(fanniemae_2023Q1['ZipShort'].unique())

import plotly.io as pio
pio.renderers.default='browser'
from urllib.request import urlopen
import json
import requests

# =============================================================================
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)
# =============================================================================

# =============================================================================
# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})
# 
# import plotly.express as px
# 
# fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 12),
#                            scope="usa",
#                            labels={'unemp':'unemployment rate'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
# 
# =============================================================================
df1 = fanniemae_2023Q1.groupby(['State'])['currint','BorrCRS','DTI'].mean()
df1.index.name = 'State'
df1.reset_index(inplace=True)

fig, ax = plt.subplots()
ax.bar(df1['State'].tolist(), df1['currint'].tolist(), align='center', width=0.8)
ax.figure(figsize = (20, 5))
ax.set_ylabel('Mean Current Interest Rate')
ax.set_xlabel('States')              
ax.set_title('Mean Current Interst Rate per State')
plt.show

# =============================================================================
# import matplotlib.pyplot as plt
# 
# fig, ax = plt.subplots()
# 
# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
# 
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
# 
# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')
# 
# plt.show()
# 
# =============================================================================
with urlopen('https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json') as response:
    states = json.load(response)

import plotly.express as px

df2 = fanniemae_2023Q1.groupby(['State'])['loanid'].count()
df2 = pd.DataFrame(df2)
df2.index.name = 'State'
df2.reset_index(inplace=True)

fig = px.choropleth(df2, locations='State', locationmode='USA-states' color='loanid',
                    
                           color_continuous_scale="Viridis",
                           range_color=(0, 1500000),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# =============================================================================
# for i in importfilelist:
#     print("fanniemae_" + (i))
#     fanniemae[i] =  "fanniemae_" + (i)
#     print(fanniemae)
#     ("fanniemae_" + (i)) = pd.read_csv(((i)+".csv"),sep='|')
#     
# =============================================================================


# =============================================================================
# importfilelist = ("2022Q1.csv", "2022Q2.csv", "2022Q3.csv", "2022Q4.csv", "2023Q1.csv")
# folder_name = 'FannieMaeMortData'
# file_type = 'csv'
# seperator ='|'
# dataframe = pd.concat([pd.read_csv(f, sep=seperator) for f in glob.glob(folder_name + "/*."+file_type)],ignore_index=True)
#     
# =============================================================================
