# -*- coding: utf-8 -*-
import pandas
import seaborn

def load_data():
    chrData = []
    year = 2014
    for i in xrange(4):
        chrData.append(pandas.read_csv("data/" + str(year) + "CHR_CSV_Analytic_Data.csv"))

    for i in xrange(4):
        chrData[i].rename(columns=lambda x: x.lower(), inplace=True)

    return chrData

def makeGraphs(dataframe, colNames, yCol):
    for col in colNames:
        dataframe.plot(y=yCol, x=col, kind="scatter")

def genCorrelation(dataframe, searchToken=""):
    values = [col for col in dataframe.columns if searchToken in col]
    correlation = dataframe.filter(values).corr()
    return correlation

def plotCorrelation(dataframe, searchToken=""):
    seaborn.heatmap(genCorrelation(dataframe, searchToken))

chrAgg = pandas.read_csv("aggregated_v2.csv", thousands=",")

corr = genCorrelation(chrAgg, "value")

for i in xrange(len(corr["drug.overdose.deaths.value_2017"])):
    val = corr["drug.overdose.deaths.value_2017"][i]
    if abs(val) > 0.3:
        print str(val) + "\t\t" + list(corr.index)[i]
