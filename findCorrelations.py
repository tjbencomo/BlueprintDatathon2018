from customLib.anaconda import printCorrelations
import pandas

data = pandas.read_csv("aggregated_v2.csv", thousands=",")
printCorrelations(data, "drug.overdose.deaths.value_2017", 0.3)
