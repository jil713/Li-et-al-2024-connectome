# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 00:37:11 2023

@author: lijin
"""

import numpy as np
import pandas as pd

#Import the raw connectivity excel sheet and clean it up
df = pd.read_excel ("Ordered GRN vs 1st TPN clustering.xlsx")
columns_to_drop = ['Name', 'Side']
df_a = df.drop(columns_to_drop,axis=1)
df_a = df_a.set_index('GRN type')
df_a.replace(np.nan, 0, inplace=True)
df_final = df_a.drop('GRN', axis=1)

#Plot the clustermap
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
clmap_big = mpl.colormaps['coolwarm']
newcmp = ListedColormap(clmap_big(np.linspace(0, 1, 256)))

lut = dict(zip(df_a.GRN.unique(), 
               ['mediumseagreen', 'purple', 'tomato', 'royalblue']))
row_colors = df_a.GRN.map(lut)

import seaborn as sns

sns.clustermap(df_final, figsize=(8,20),
               method = 'average', metric="correlation", 
               cmap = newcmp, row_cluster=False, row_colors=row_colors)
plt.show()