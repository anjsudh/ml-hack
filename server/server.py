from flask import Flask, jsonify, request
import flask_cors

from predictors.disease_predictor import disease_predictor, add_data_to_model
from predictors.symptom_predictor import predict_next_symptoms

app = Flask(__name__)
flask_cors.CORS(app)

import pandas as pd


@flask_cors.cross_origin()
@app.route('/symptoms', methods=['OPTIONS', 'GET'])
def getSymptoms():
    if request.method == 'OPTIONS':
        return jsonify({})
    data = pd.read_csv("../data/trial2/disease_prediction_input.csv", header=0, sep=';')
    symptoms = list(data.columns.values)
    return jsonify(symptoms[0:-1])


@flask_cors.cross_origin()
@app.route('/symptoms/predict', methods=['OPTIONS', 'POST'])
def getNextSymptoms():
    if request.method == 'OPTIONS':
        return jsonify({})
    data = request.get_json()
    positives = data['positives']
    negatives = data['negatives']
    possible_symptoms = predict_next_symptoms(positives, negatives)
    possible_symptoms = sorted(possible_symptoms[0], key=lambda x: x[1], reverse=True)
    possible_symptoms_new = []
    for pd in possible_symptoms:
        if pd[0] not in possible_symptoms_new:
            possible_symptoms_new.append(pd[0])
    return jsonify(possible_symptoms_new)


@flask_cors.cross_origin()
@app.route('/diseases/predict', methods=['OPTIONS', 'POST'])
def getNextDiseases():
    if request.method == 'OPTIONS':
        return jsonify({})
    data = request.get_json()
    positives = data['positives']
    possible_diseases = sorted(disease_predictor(positives), key=lambda x: x[1], reverse=True)
    return jsonify(possible_diseases)

@flask_cors.cross_origin()
@app.route('/symptoms/diseases', methods=['OPTIONS', 'POST'])
def saveEntry():
    if request.method == 'OPTIONS':
        return jsonify({})
    data = request.get_json()
    symptoms = data['symptoms']
    diseases = data['disease']
    add_data_to_model(symptoms, diseases);
    return ("",201)


@app.route('/predict', methods=["POST"])
def predict():
    positives = request.json.get("positives")
    negatives = request.json.get("negatives")

    possible_diseases = sorted(disease_predictor(positives), key=lambda x: x[1], reverse=True)

    possible_symptoms = predict_next_symptoms(positives, negatives)[0]
    possible_symptoms = sorted(possible_symptoms, key=lambda x: x[1], reverse=True)

    possible_symptoms_new = []
    for pd in possible_symptoms:
        if pd[0] not in possible_symptoms_new:
            possible_symptoms_new.append(pd[0])
    result = {"possibleSymptoms": possible_symptoms_new, "possibleDiseases": possible_diseases}
    return jsonify(result)

if __name__ == '__main__':
    app.run()
