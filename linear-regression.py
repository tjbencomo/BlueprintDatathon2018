import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.externals import joblib 
from sklearn import linear_model
import timeit


print "Libraries loaded"


dataset_path = '/home/users/tbencomo/blueprint/clean_aggregated.csv'
data = pd.read_csv(dataset_path)

regressor = linear_model.LinearRegression(n_jobs=-1)

pipeline = make_pipeline(preprocessing.StandardScaler(), regressor)


df = pd.read_csv('/home/users/tbencomo/blueprint/corrAbovePoint3.txt', sep='\t', header = None)
df = df.drop(1, axis=1)
value_cols = df[2].tolist()

y = data['drug.overdose.deaths.value_2017']
X = data.filter(value_cols)
X = data.drop('drug.overdose.deaths.value_2017', axis = 1)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=523)

print list(X_train)


hyperparameters = {'normalize': [True]}

#clf = GridSearchCV(regressor, hyperparameters, cv=10, verbose = 3, n_jobs = -1)

regressor.fit(X_train, y_train)

print "Begin model training"

#clf.fit(X_train, y_train)

print "Model fit"

coefs = pd.DataFrame(list(X_train), regressor.coef_)

print('Coefficients: \n', regressor.coef_)

with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
    print(coefs)


pred = regressor.predict(X_test)

np.savetxt('predicted_values.csv', pred, delimiter = ',')
np.savetxt('y_values.csv', y_test, delimiter = ',')

print r2_score(y_test, pred)
print mean_squared_error(y_test, pred)

#joblib.dump(clf, 'logistic_regressor2.pkl')


