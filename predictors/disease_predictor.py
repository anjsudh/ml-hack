import pickle

import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("../data/trial2/disease_prediction_input.csv", header=0, sep=';')
headers = list(data.columns.values)
y = data.iloc[:, -1].values

def add_data_to_model(symptoms, disease):
    with open('../resources/state/disease_model.pkl', 'rb') as input_file:
        global model
        model = pickle.load(input_file)
    X = np.zeros(len(headers)-1);
    for symptom in symptoms:
        index = headers.index(symptom)
        if index > -1:
            X[index] = 1
    X = X.reshape(1, -1)
    Y = np.asarray(disease)
    Y = np.reshape(Y, 1)
    model = model.partial_fit(X, Y)
    with open('../resources/state/disease_model.pkl', 'wb') as output_file:
        pickle.dump(model, output_file)


def load_disease_data_into_model():
    data = pd.read_csv("../data/trial2/disease_prediction_input.csv", header=0, sep=';')
    x = data.iloc[:, 0:-1].values
    y = data.iloc[:, -1].values
    mnb = MultinomialNB()
    mnb = mnb.fit(x, y)

    with open('../resources/state/disease_model.pkl', 'wb') as output_file:
        pickle.dump(model, output_file)


def disease_predictor(symptoms):
    with open('../resources/state/disease_model.pkl', 'rb') as input_file:
        global model
        model = pickle.load(input_file)

    sample_row = np.zeros(len(headers) - 1);
    for symptom in symptoms:
        index = headers.index(symptom)
        if index > -1:
            sample_row[index] = 1
    diseases = list(set(y));
    diseases.sort();
    sample_row = sample_row.reshape(1, -1)
    y_pred = list(model.predict_proba(sample_row)[0])
    results = [];
    for i in range(len(y_pred)):
        max = y_pred.index(np.amax(y_pred))
        results.append((diseases[max], y_pred[max]))
        y_pred[max] = -100
    return results
