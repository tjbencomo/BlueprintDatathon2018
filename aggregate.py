# -*- coding: utf-8 -*-
#Spyder Editor
import pandas as pd
#run this script to produce an updated version of the aggregated data
df14 = pd.read_csv("./data/2014CHR_CSV_Analytic_Data.csv")
df15 = pd.read_csv("./data/2015CHR_CSV_Analytic_Data.csv")
df16 = pd.read_csv("./data/2016CHR_CSV_Analytic_Data.csv")
df17 = pd.read_csv("./data/2017CHR_CSV_Analytic_Data.csv")

df14.rename(columns=lambda x: x.lower(), inplace=True)
df15.rename(columns=lambda x: x.lower(), inplace=True)
df16.rename(columns=lambda x: x.lower(), inplace=True)
df17.rename(columns=lambda x: x.lower(), inplace=True)

necessary = ["drug.poisoning.deaths.value"]
df14.dropna(subset=necessary, inplace=True)
df15.dropna(subset=necessary, inplace=True)
#
necessary = ["drug.overdose.deaths.value"]
df16.dropna(subset=necessary, inplace=True)
df17.dropna(subset=necessary, inplace=True)

df14.dropna(axis=1, thresh=df14['statecode'].count() - 150, inplace=True)
df15.dropna(axis=1, thresh=df15['statecode'].count() - 150, inplace=True)
df16.dropna(axis=1, thresh=df16['statecode'].count() - 150, inplace=True)
df16.dropna(axis=1, thresh=df17['statecode'].count() - 150, inplace=True)

df14.set_index(['statecode', 'county'])
df15.set_index(['statecode', 'county'])
df16.set_index(['statecode', 'county'])
df17.set_index(['statecode', 'county'])

df14.rename(columns=lambda x: x + "_2014", inplace=True)
df15.rename(columns=lambda x: x + "_2015", inplace=True)
df16.rename(columns=lambda x: x + "_2016", inplace=True)
df17.rename(columns=lambda x: x + "_2017", inplace=True)

df = pd.concat([df14, df15, df16, df17], axis=1).sort_index(axis=1)

df.to_csv("aggregated_update.csv")