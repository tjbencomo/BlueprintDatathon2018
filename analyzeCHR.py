import csv
from analysisModules import *

data = loadData()

#writeListToFile("columnNames.txt", getLabels(loadCSV("2017CHR_CSV_Analytic_Data_v2.csv"), rowIndex = 0))


# stateIndices = [0, 0, 0, 1]
# countyIndices = [1, 1, 1, 2]
#
# missing = []
# names = ["Drug.Poisoning.Value", "Drug.poisoning.deaths.Value", "Drug.Overdose.Deaths.Value", "Drug.Overdose.Deaths.Value"]
# for i in xrange(4):
#     index = getColIndex(data[i][0], names[i])
#     missing.append([])
#     for row in data[i]:
#         if row[index] == "":
#             missing[i].append(str(row[stateIndices[i]]) + str(row[countyIndices[i]]))
#
# missingInAll = intersect(missing)
# print len(missingInAll)
