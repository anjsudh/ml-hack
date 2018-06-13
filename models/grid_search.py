import timeit

import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("../data/trial2/disease_prediction_input.csv", header=0, sep=';')
headers = list(data.columns.values)
x = data.iloc[:, 0:-1].values
y = data.iloc[:, -1].values
from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.svm import SVC

classifier = SVC(kernel='linear')
classifier = classifier.fit(x, y)
Y_pred = classifier.predict(X_test)

from sklearn.grid_search import GridSearchCV

# parameters = {'kernel':('linear', 'rbf'), 'C':[1,2, 5, 10]}
# parameters = {'kernel':('linear', 'poly', 'rbf', 'sigmoid'), 'C':[1,2]}
# parameters = {'C':[0.5,1]}
# parameters = {'C':[0.01,0.1,0.5]}
# parameters = {'C':[0.3,0.4,0.5,0.6,0.7]}
# parameters = {'C':[0.7,0.8,0.9]}
# parameters = {'C':[0.65,0.7,0.75]}
parameters = {'C':[0.64, 0.65,0.66]}
grid_search = GridSearchCV(estimator=classifier,
                           param_grid=parameters,
                           scoring='accuracy')
grid_search = grid_search.fit(x, y)
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_
print(best_accuracy)
print(best_parameters)
