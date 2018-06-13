import random
import pandas as pd

data = pd.read_csv("../data/trial2/symptoms.csv", encoding="ISO-8859-1")
cols = data.columns.tolist()
cols = [cols[1]] + [cols[0]]
data = data[cols]
data = data.drop_duplicates()
data.to_csv("../data/trial2/symptoms_diseases_mapping.csv", index=False, sep=";")

data = pd.read_csv("../data/trial2/symptoms_diseases_mapping.csv", sep=";", encoding="ISO-8859-1")
df = pd.DataFrame(data)
df_1 = pd.get_dummies(df.symptom_name)
df_s = df['disease_common_name']
df_pivoted = pd.concat([df_1, df_s], axis=1)
df_pivoted.drop_duplicates(keep='first', inplace=True)
df_pivoted = df_pivoted.groupby('disease_common_name').sum()
df_pivoted = df_pivoted.reset_index()
cols = df_pivoted.columns.tolist()
cols = cols[1:] + [cols[0]]
df_pivoted = df_pivoted[cols]
df_pivoted.to_csv("../data/trial2/symptoms_disease_pivoted.csv", index=False, sep=";")

weight_data = pd.read_csv("../data/trial2/symptoms.csv", encoding="ISO-8859-1")
data = pd.read_csv("../data/trial2/symptoms_disease_pivoted.csv", encoding="ISO-8859-1", sep=";")
columns = list(data.columns.values)
resultData = data.copy()
for index, row in data.iterrows():
    disease_name = row[-1]
    indices = [i for i in range(0, len(columns) -1) if row[i] == 1.0]
    print(disease_name)
    NO_OF_DUPLICATES = weight_data.loc[weight_data['disease_common_name'] == disease_name].values[0][2]
    for i in range(0, int(NO_OF_DUPLICATES)):
        df_try = data.loc[data['disease_common_name'] == disease_name]
        df_try = df_try.copy()
        if len(indices) > 1:
            df_try[data.columns[indices[random.randint(0, len(indices)-1)]]] = 0
        resultData = resultData.append(df_try, ignore_index=True)
resultData.to_csv("../data/trial2/disease_prediction_input.csv", index=False, sep=";")


data = pd.read_csv("../data/trial2/symptoms_disease_pivoted.csv", encoding="ISO-8859-1", sep=";")
columns = list(data.columns.values)
with open("../data/trial2/symptoms_disease_pivoted.csv") as inp, open("../data/trial2/apriori_input_partial.csv", 'w') as o1:
    next(inp)
    for line in inp:
        symptoms = line.strip('\n').split(';')
        disease = symptoms.pop()
        present_symptoms = [columns[indx] for indx, val in enumerate(symptoms) if val == "1.0"]
        if len(present_symptoms) > 1:
            present_symptoms = ";".join(present_symptoms)
            o1.write("{}\n".format(present_symptoms))


dataset = pd.DataFrame()
with open("../data/trial2/apriori_input_partial.csv", 'r', errors = 'ignore') as f:
    for line in f:
        dataset = pd.concat( [dataset, pd.DataFrame([tuple(line.strip().split(';'))])], ignore_index=True )
        dataset = dataset.drop_duplicates()
print("data read")
with open("../data/trial2/apriori_input.csv", 'w', errors = 'ignore') as f:
    for i in range(0, len(dataset.index)):
        f.write("\n"+(";".join([str(dataset.values[i,j]) for j in range(0, len(dataset.columns)) if str(dataset.values[i,j]) != 'nan'])))
print("converted to transactions")