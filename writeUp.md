# Predictors of Drug Overdose Deaths

## Notes
Python Version: `python-2.7`
Dependencies: `csv`, `pandas`, `math`, `seaborn`, `scipy`
Modules Structure:
```
customLib
|- analysis: Contains more general analysis functions
|- anaconda: Contains anaconda-specific functions, particularly those using panda
```

## Data Processing and Sanitization

* Remove `measure` rows present in some years of data
* Sanitize column names by replacing spaces (` `) and hyphens (`-`) with dots (`.`)
* Make all column names lowercase
* Exclude any counties lacking values for drug overdose deaths
* Aggregate data from all 4 years into one CSV file with column names in the form
`column.name_year`, ensuring that counties line up across years. Exclude counties
missing from any year.
* Delete any blank columns
* Replace all remaining blank cells with mean for that cell's respective column (compute mean excluding blank cells)

## Factor Selection
This operation is fulfilled by `findCorrelations.py`, which performs the following
operations on the file `aggregated_v2.csv`:
* Calculate the correlation coefficient between all columns containing `value`
and the column `drug.overdose.deaths.value_2017`
* For all coefficients with an absolute value greater than `0.3`, print the
coefficient and the column name separated by a tab (`\t`)

## Linear Regression Modeling

## Model Prediction Testing

### Thingy Tomas Did

### Statistical Analysis of Results
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
