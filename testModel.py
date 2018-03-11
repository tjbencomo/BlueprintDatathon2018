from customLib import analysis
from scipy.stats import ttest_ind
from scipy.stats import tstd
import pandas

predicted = analysis.loadFloats("results/predicted.txt")
actual = analysis.loadFloats("results/actual.txt")

print "Mean Squared Error: " + str(analysis.mse(predicted, actual))
print "Range of Predicted: " + str(min(predicted)) + " - " + str(max(predicted))
print "Range of Actual: " + str(min(actual)) + " - " + str(max(actual))
print "Mean of Predicted: " + str(sum(predicted) / len(predicted))
print "Mean of Actual: " + str(sum(actual) / len(actual))
print "Standard Deviation of Predicted: " + str(tstd(predicted))
print "Standard Deviation of Actual: " + str(tstd(actual))
print "T-Test p-value: " + str(ttest_ind(predicted, actual)[1])

dataframe = pandas.DataFrame(data={"predicted":predicted, "actual":actual})
dataframe.plot(x="predicted", y="actual", kind="scatter")
