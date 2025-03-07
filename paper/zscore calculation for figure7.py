# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:06:13 2025

@author: User
"""

import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.stats import zscore

dfs = []

for i in range(0, 1000):
    excel_file = f'probability_{i}.xlsx'
    df = pd.read_excel(excel_file, index_col=0)
    dfs.append(df)

combined_df = pd.concat(dfs, axis=1)
concatenated_df = combined_df.mean(axis=0)

df_actual=pd.read_excel('pruned_actual_probability.xlsx')
actual_mean=df_actual.mean(axis=0)

shuffled_mean = np.mean(concatenated_df)
shuffled_std = np.std(concatenated_df)

shuffled_zscores = (concatenated_df-shuffled_mean)/shuffled_std
actual_zscore = (actual_mean-shuffled_mean)/shuffled_std

ci_lower, ci_upper = np.percentile(shuffled_zscores, [2.5, 97.5])

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.hist(shuffled_zscores, bins=20, color='grey', edgecolor=None)
plt.hist(actual_zscore, color='tomato', edgecolor=None)
#plt.axvline(9.13542, color="tomato", linewidth=1.5)
plt.axvline(ci_lower, color='mediumseagreen', linestyle='dashed', linewidth=1.5, label='95% CI Lower (-1.96)')
plt.axvline(ci_upper, color='mediumseagreen', linestyle='dashed', linewidth=1.5, label='95% CI Upper (1.96)')
plt.rcParams['pdf.fonttype'] = 42