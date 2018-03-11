import csv

def intersect(lists):
    intersection = []
    for item in lists[0]:
        if foundInAll(lists[1:], item):
            intersection.append(item)
    return intersection

def foundInAll(lists, target):
    for lst in lists:
        if target not in lst:
            return False
    return True

def printExclusion(message):
    print message

def printRemoval(message):
    print message

def writeListToFile(filename, list):
    with open(filename, 'w') as f:
        for item in list:
            f.write(item + "\n")

def getColIndex(row, target):
    for i in xrange(len(row)):
        if row[i] == target:
            return i
    return -1

def loadCSV(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            newRow = []
            for item in row:
                newRow.append(item)
            data.append(newRow)
    return data

def getNumBlank(data, col):
    blank = 0
    for row in data:
        if row[col] == "":
            blank = blank + 1
    return blank

def getLabels(data, rowIndex, startCol = 0, include = "", exclude = "", blankThreshold = -1):
    if blankThreshold == -1:
        blankThreshold = len(data)
    labels = []
    row = data[rowIndex]
    for i in xrange(len(row) - startCol):
        col = i + startCol
        item = row[col]
        if include in item:
            if not (exclude != "" and exclude in item):
                blanks = getNumBlank(data, col)
                if not blanks >= blankThreshold:
                    labels.append(item)
                else:
                    printExclusion ("Excluding (too many blanks: " + str(blanks) + "): " + item)
            else:
                printExclusion ("Excluding (contains " + exclude + "): " + item)
        else:
            printExclusion ("Excluding (missing " + include + "): " + item)
    return labels

def getCommonLabels(data):
    commonLabels = getLabels(data = data[0], rowIndex = 1, startCol = 6, blankThreshold = 150)
    year = 2015
    for dataset in data[1:]:
        labels = getLabels(data = dataset, rowIndex = 0, startCol = 6, blankThreshold = 150)
        toRemove = []
        for label in commonLabels:
            if label not in labels:
                toRemove.append(label)
                printRemoval ("Removing (not in " + str(year) + "): " + label)
        for label in toRemove:
            commonLabels.remove(label)
        year = year + 1
    return commonLabels

def loadData():
    data = []
    data.append(loadCSV("data/2014CHR_CSV_Analytic_Data.csv"))
    data.append(loadCSV("data/2015CHR_CSV_Analytic_Data.csv"))
    data.append(loadCSV("data/2016CHR_CSV_Analytic_Data.csv"))
    data.append(loadCSV("data/2017CHR_CSV_Analytic_Data.csv"))
    return data

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
