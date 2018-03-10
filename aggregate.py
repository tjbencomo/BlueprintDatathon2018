# -*- coding: utf-8 -*-
#Spyder Editor
import pandas as pd
df14 = pd.read_csv("data/2014CHR_CSV_Analytic_Data.csv")
df15 = pd.read_csv("data/2015CHR_CSV_Analytic_Data.csv")
df16 = pd.read_csv("data/2016CHR_CSV_Analytic_Data.csv")
df17 = pd.read_csv("data/2017CHR_CSV_Analytic_Data.csv")

fname = "usefulCols.txt"

with open(fname) as f:
    usefulCols = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
usefulCols = [x.strip() for x in usefulCols]

df14.rename(columns=lambda x: x.lower(), inplace=True)
print usefulCols
for column in df14:
    if not column in usefulCols:
        df14.drop(columns=[column], inplace=True)
df14.rename(columns=lambda x: x + "14", inplace=True)

df15.rename(columns=lambda x: x.lower(), inplace=True)
for column in df15:
    if not column in usefulCols:
        df15.drop(columns=[column], inplace=True)
df15.rename(columns=lambda x: x + "15", inplace=True)
        
df16.rename(columns=lambda x: x.lower(), inplace=True)
for column in df16:
    if not column in usefulCols:
        df16.drop(columns=[column], inplace=True)
df16.rename(columns=lambda x: x + "16", inplace=True)

df17.rename(columns=lambda x: x.lower(), inplace=True)
for column in df17:
    if not column in usefulCols:
        df17.drop(columns=[column], inplace=True)
df17.rename(columns=lambda x: x + "17", inplace=True)
        
result = pd.concat([df14, df15, df16, df17], axis=1)
result.sort_index(axis=1, inplace=True)
toDrop = set()
for column in result:
    short = column[:-2]
    if not {short + "14", short + "15", short + "16", short + "17"}.issubset(result.columns):
        toDrop.add(column)
for column in toDrop:
    result.drop(columns=[column], inplace=True)
for column in result:
    print(column)
print(len(result.columns))
result.to_pickle("combined")
#This is a temporary script file.

