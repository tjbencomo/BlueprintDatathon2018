# Identifying Causes of Drug Overdoses

As part of Stanford's Blueprint Datathon 2018, this repository contains our
work in identifying causes and remediation strategies for drug overdoses.

## Notes
Python Version: `python-2.7`

Dependencies: `csv`, `pandas`, `math`, `seaborn`, `scipy`

Modules Structure:
```
customLib
|- analysis: Contains more general analysis functions
|- anaconda: Contains anaconda-specific functions, particularly those using panda
```

## Methodology

### Data Processing and Sanitization

* Remove `measure` rows present in some years of data
* Sanitize column names by replacing spaces (` `) and hyphens (`-`) with dots (`.`)
* Make all column names lowercase
* Exclude any counties lacking values for drug overdose deaths
* Aggregate data from all 4 years into one CSV file with column names in the form
`column.name_year`, ensuring that counties line up across years. Exclude counties
missing from any year.
* Delete any blank columns
* Replace all remaining blank cells with mean for that cell's respective column (compute mean excluding blank cells)

### Factor Selection
This operation is fulfilled by `findCorrelations.py`, which performs the following
operations on the file `aggregated_v2.csv`:
* Calculate the correlation coefficient between all columns containing `value`
and the column `drug.overdose.deaths.value_2017`
* For all coefficients with an absolute value greater than `0.3`, print the
coefficient and the column name separated by a tab (`\t`)

### Linear Regression Modeling

To better understand the key factors underlying the drug deaths per county, we built a linear regression model to predict drug deaths in the future given certain information about a county. This regression model, using ordinary least regression, was trained on a subset of features from the CHS dataset. We tried predicting drug overdose deaths in 2017 by county based on county information from previous years. A full list of features can be found in the script output in linear-regression.py in our github. To train the model, we split our data into 60% train data and 40% test data. From there we ran the model with the cross validation algorithm with k = 10. This model was then tested on the 40% test data, and achieved a mean squared error score of 9.09. The r squared value for our model was .8699. We then analyzed the coefficients for each feature from our model, which provided more insight into exactly which features play a key role in drug deaths.

#### Statistical Analysis of Results
Write the model's prediction for each county in the testing data to a text file
with one prediction per line. **HOW DO YOU DO THIS** Repeat for the actual
testing data. These files should be `results/actual.txt` and `results/predicted.txt`
for the script `testModel.py` to work. This script performs the following:
* Computes the following statistics:
  * Mean squared error (MSE) between predicted and actual values
  * Ranges of predicted and actual data
  * Standard deviations of predicted and actual data
  * p-value from Independent T-Test on predicted and actual data
* Displays a scatter plot of actual versus predicted results (may only work
  when script is run in `spyder`)

## License

Copyright (c) U8N WXD, Tomas Bencomo, and Ketan Agrawal 2018
All Rights Reserved
