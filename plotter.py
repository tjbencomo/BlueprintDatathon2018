# -*- coding: utf-8 -*-
import pandas
import numpy

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

with open ("valueNames.txt", 'r') as f:
    for line in f:
        valueNames.append(line[:-1])

chr2017.fillna(0)
numericCols = chr2017.select_dtypes(include=[numpy.number])

for col in valueNames:
    chr2017.plot(y="drug.overdose.deaths.value", x=col, kind="scatter")