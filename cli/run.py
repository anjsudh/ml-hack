from predictors.disease_predictor import disease_predictor, add_data_to_model
from predictors.symptom_predictor import predict_next_symptom

positives = []
negatives = []
next_symptom = input("What symptom you got?\n")
symptom_ans = 'y'
while True:
    if symptom_ans == 'y':
        positives.append(next_symptom)
    if symptom_ans == 'n':
        negatives.append(next_symptom)
    next_symptom = predict_next_symptom(positives, negatives)
    diseases = disease_predictor(positives)[0:3]
    print("Possible Diseases: \n", diseases);
    print("\n")
    if next_symptom is None:
        add_data_to_model(positives, diseases[0][0])
        break
    symptom_ans = input("Do you have '{}' (y/n)\n".format(next_symptom))



