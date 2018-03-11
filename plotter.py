# -*- coding: utf-8 -*-
import pandas
import numpy
import seaborn

def loadData():
    chrData = []
    year = 2014
    for i in xrange(4):
        chrData.append(pandas.read_csv("data/" + str(year) + "CHR_CSV_Analytic_Data.csv"))
    
    for i in xrange(4):
        chrData[i].rename(columns=lambda x: x.lower(), inplace=True)
    
    return chrData

chr2017 = pandas.read_csv("2017CHR_CSV_Analytic_Data_v2.csv", thousands=",")

interestingCols = ["uninsured.value", "primary.care.physicians.value", 
                   "mental.health.providers.value", "preventable.hospital.stays.value",
                   "high.school.graduation.value", "some.college.value", 
                   "unemployment.value", "children.in.poverty.value",
                   "income.inequality.value", "violent.crime.value", 
                   "food.insecurity.value", "health.care.costs.value",
                   "median.household.income.value", "percent.of.population.that.is.female"]

valueNames = []

with open ("2017valueNames.txt", 'r') as f:
    for line in f:
        valueNames.append(line[:-1])

chr2017.fillna(0)
numericCols = chr2017.select_dtypes(include=[numpy.number])

def makeGraphs(dataframe, colNames, yCol):
    for col in colNames:
        dataframe.plot(y=yCol, x=col, kind="scatter")

def plotCorrelation(dataframe, searchToken = ""):
    values = [col for col in dataframe.columns if searchToken in col]
    correlation = dataframe.filter(values).corr()
    seaborn.heatmap(correlation)

plotCorrelation(chr2017, "value")