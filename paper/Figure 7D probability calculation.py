# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:06:05 2024

@author: lijin
"""
import pandas as pd
import numpy as np

#Import 1000 shuffled excel sheets, assign variables, and store them in a list
dfs = []

for i in range(1, 1001):
    excel_file = f'randomized_{i}.xlsx'
    df = pd.read_excel(excel_file, index_col=0)
    dfs.append(df)

for i, df in enumerate(dfs, start=1):
    globals()[f'df{i}'] = df

#Calculate probabilities of 2 TPNs belonging to the same cluster
for file_num in range(1,1001):
    file_name = f'probability_{file_num}.xlsx'
    
    #Assign cluster labels based on the morphological clustering result
    for df_n in dfs:
        clusterlabel=[1]*33+[2]*53+[3]*33+[4]*36
        df_n['clusterlabel'] = clusterlabel
        df_cluster = df_n.set_index('clusterlabel')

        cluster1=df_cluster.iloc[0:33,:]
        cluster2=df_cluster.iloc[33:86,:]
        cluster3=df_cluster.iloc[86:119,:]
        cluster4=df_cluster.iloc[119:155,:]
            
        clus1counts_list = []

        for column1 in cluster1.columns:
            num_entries_clus1 = cluster1[column1].count()
            clus1counts_list.append(num_entries_clus1)
    
        clus2counts_list = []
        
        for column2 in cluster2.columns:
            num_entries_clus2 = cluster2[column2].count()
            clus2counts_list.append(num_entries_clus2)

        clus3counts_list = []

        for column3 in cluster3.columns:
            num_entries_clus3 = cluster3[column3].count()
            clus3counts_list.append(num_entries_clus3)

        clus4counts_list = []

        for column4 in cluster4.columns:
            num_entries_clus4 = cluster4[column4].count()
            clus4counts_list.append(num_entries_clus4)

        totalcounts_list = []

        for column_sum in df_cluster.columns:
            num_entries_sum = df_cluster[column_sum].count()
            totalcounts_list.append(num_entries_sum)

        df_clustercounts = pd.DataFrame({
            'Cluster1': clus1counts_list,
            'Cluster2': clus2counts_list,
            'Cluster3': clus3counts_list,
            'Cluster4': clus4counts_list
            })

        df_totalcounts = pd.DataFrame({
            'Total': totalcounts_list})

        list_totalcounts = df_totalcounts.values.flatten().tolist()

        import math
            
        list_comb = []

        for n in list_totalcounts:
            combination  = math.comb(n,2)
            list_comb.append(combination)

        list_cluster1 = []

        for n in clus1counts_list:
            combination = math.comb(n,2)
            list_cluster1.append(combination)

        list_cluster2 = []

        for n in clus2counts_list:
            combination = math.comb(n,2)
            list_cluster2.append(combination)

        list_cluster3 = []

        for n in clus3counts_list:
            combination = math.comb(n,2)
            list_cluster3.append(combination)

        list_cluster4 = []

        for n in clus4counts_list:
            combination = math.comb(n,2)
            list_cluster4.append(combination)

        comb_sumeachcluster = [sum(x) for x in zip(list_cluster1, list_cluster2, list_cluster3, list_cluster4)]

        df_combsumeachcluster = pd.DataFrame({
            'sum combination_each cluster': comb_sumeachcluster})

        probability = df_combsumeachcluster.div(list_comb, axis=0)
        probability.to_excel(file_name)
