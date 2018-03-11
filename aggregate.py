# -*- coding: utf-8 -*-
#Spyder Editor
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df14 = pd.read_csv("./data/2014CHR_CSV_Analytic_Data.csv")
df15 = pd.read_csv("./data/2015CHR_CSV_Analytic_Data.csv")
df16 = pd.read_csv("./data/2016CHR_CSV_Analytic_Data.csv")
df17 = pd.read_csv("./data/2017CHR_CSV_Analytic_Data.csv")

def plot_corr(df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);

#df17 = pd.read_csv("2017CHR_CSV_Analytic_Data_v2.csv")
##plot_corr(df17, size=20)
#corr = df17.corr()
#drugs = corr['drug.overdose.deaths.value']
#print drugs.sort_values().to_string()
#sns.heatmap(corr, 
#            xticklabels=corr.columns.values,
#            yticklabels=corr.columns.values)

df14.rename(columns=lambda x: x.lower(), inplace=True)
df15.rename(columns=lambda x: x.lower(), inplace=True)
df16.rename(columns=lambda x: x.lower(), inplace=True)
df17.rename(columns=lambda x: x.lower(), inplace=True)
#df17.rename(columns=lambda x: x.lower(), inplace=True)
#
necessary = ["drug.poisoning.deaths.value"]
df14.dropna(subset=necessary, inplace=True)
df15.dropna(subset=necessary, inplace=True)
#
necessary = ["drug.overdose.deaths.value"]
df16.dropna(subset=necessary, inplace=True)
df17.dropna(subset=necessary, inplace=True)
#print(df17.shape)
#df17.dropna(subset=necessary, inplace=True)
#print(df17.shape)
df14.dropna(axis=1, thresh=df14['statecode'].count() - 150, inplace=True)
df15.dropna(axis=1, thresh=df15['statecode'].count() - 150, inplace=True)
df16.dropna(axis=1, thresh=df16['statecode'].count() - 150, inplace=True)
df16.dropna(axis=1, thresh=df17['statecode'].count() - 150, inplace=True)

df14.set_index(['statecode', 'countycode'])
df15.set_index(['statecode', 'countycode'])
df16.set_index(['statecode', 'countycode'])
df16.set_index(['statecode', 'countycode'])

df14.rename(columns=lambda x: x + "_2014", inplace=True)
df15.rename(columns=lambda x: x + "_2015", inplace=True)
df16.rename(columns=lambda x: x + "_2016", inplace=True)
df17.rename(columns=lambda x: x + "_2017", inplace=True)

df = pd.concat([df14, df15, df16, df17], axis=1).sort_index(axis=1)
print(df)
df.to_csv("aggregated.csv")

#corr = df14.corr()
#drugs1 = corr['drug.poisoning.deaths.value']
#
#corr = df15.corr()
#drugs2 = corr['drug.poisoning.deaths.value']
#
#corr = df16.corr()
#drugs3 = corr['drug.overdose.deaths.value']
#
#dftot = pd.concat(drugs1, drugs2, drugs3, axis=1, keys='')
#for column in df17.select_dtypes(include=np.number):
#    df17.plot(x='drug.overdose.deaths.value', y=column, kind='scatter')

#df17.to_csv("2017CHR_CSV_Analytic_Data_v2.csv")
#print(df17.shape)
#for column in df17.select_dtypes(include=np.number):
#    df17.plot(x='drug.overdose.deaths.value', y=column, kind='scatter')

#df17.to_csv("2017CHR_CSV_Analytic_Data_v2.csv")

#df14.rename(columns=lambda x: x + "14", inplace=True)
#df15.rename(columns=lambda x: x + "15", inplace=True)
#df16.rename(columns=lambda x: x + "16", inplace=True)
#df17.rename(columns=lambda x: x + "17", inplace=True)
#
##df = pd.concat([df14, df15, df16, df17], axis=1)
#
##fname = "usefulCols.txt"
##with open(fname) as f:
##    usefulCols = f.readlines()
##usefulCols = [x.strip() for x in usefulCols]
#
##for column in df:
##    if not column in usefulCols:
##        df.drop(columns=[column], inplace=True)
#
#df.dropna(axis=1, thresh=len(df.columns) - 150)
#df.sort_index(axis=1, inplace=True)
#toDrop = set()
#for column in df:
#    short = column[:-2]
#    if not {short + "14", short + "15", short + "16", short + "17"}.issubset(df.columns):
#        toDrop.add(column)
#for column in toDrop:
#    df.drop(columns=[column], inplace=True)
#
#df.sort_index(axis=1, inplace=True)
#df.to_pickle("combined")

