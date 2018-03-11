import analysisModules
from scipy.stats import ttest_ind
from scipy.stats import tstd
import pandas

def loadFloats(filename):
    vals = []
    with open(filename, 'r') as f:
        for line in f:
            vals.append(float(line[:-1]))
    return vals

predicted = loadFloats("results/predicted.txt")
actual = loadFloats("results/actual.txt")

print "Mean Squared Error: " + str(analysisModules.mse(predicted, actual))
print "Range of Predicted: " + str(min(predicted)) + " - " + str(max(predicted))
print "Range of Actual: " + str(min(actual)) + " - " + str(max(actual))
print "Standard Deviation of Predicted: " + str(tstd(predicted))
print "Standard Deviation of Actual: " + str(tstd(actual))
print "T-Test p-value: " + str(ttest_ind(predicted, actual)[1])

dataframe = pandas.DataFrame(data={"predicted":predicted, "actual":actual})
dataframe.plot(x="predicted", y="actual", kind="scatter")
