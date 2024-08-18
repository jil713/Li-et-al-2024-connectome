# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:05:47 2024

@author: lijin
"""
import pandas as pd
import numpy as np

dfs = []

for i in range(1, 21):
    excel_file = f'random_probability_{i}.xlsx'
    df = pd.read_excel(excel_file, index_col=0)
    dfs.append(df)


bin_width = 0.1
bins = np.arange(0, 1.1, bin_width)

all_counts = []

#Iterate through each shuffled Dataframe
for df in dfs:
    #Calculate counts for each bin
    counts, _ = np.histogram(df.iloc[:, 0], bins=bins)
    all_counts.append(counts)

#Calculate the average counts for each bin across all datasets
average_counts = np.mean(all_counts, axis=0)
df_average_counts = pd.DataFrame({
    'Bin_Start': bins[:-1],
    'Bin_End': bins[1:],
    'Average_Counts': average_counts
})


df_actual=pd.read_excel('actual_probability.xlsx')

#Plot the actual vs shuffled probability distribution
import seaborn as sns
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,2, figsize= [10,5])

####################################################################################
sns.histplot(df_actual.iloc[:, 0], kde=False, binwidth=0.1, color='tomato', alpha = 0, edgecolor='tomato', element="step", lw=2, ax=ax[0])

ax [0].set_ylim ([0,20])
ax [0].set_xlim ([0,1])
ax [0].spines['top'].set_visible(False)
ax [0].spines['right'].set_visible(False)
ax [0].set_xlabel ('Probability', fontsize = 10)

###################################################################################

sns.histplot(data=df_average_counts, x='Bin_Start', weights='Average_Counts', bins='auto', kde=False, alpha = 0, 
             color='grey', edgecolor='grey', element="step", lw=2, ax=ax[0])

ax [0].set_ylim ([0,20])
ax [0].set_xlim ([0,1])
ax [0].spines['top'].set_visible(False)
ax [0].spines['right'].set_visible(False)
ax [0].set_xlabel ('Probability', fontsize = 10)

