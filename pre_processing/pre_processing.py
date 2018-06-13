import random

from config import NO_OF_DUPLICATES

data = pd.read_table("../data/trial1/symptoms_source_2.tsv", encoding="ISO-8859-1")
cols = data.columns.tolist()
cols = [cols[0]] + [cols[-1]]
data = data[cols]
data = data.drop_duplicates()
data.to_csv("../data/trial1/symptoms_diseases_mapping_source_2.csv", index=False, sep=";")

data = pd.read_csv("../data/trial1/symptoms_source_1.csv", encoding="ISO-8859-1")
cols = data.columns.tolist()
cols = [cols[0]] + [cols[1]]
data = data[cols]
data = data.drop_duplicates()
data.to_csv("../data/trial1/symptoms_diseases_mapping_source_1.csv", index=False, sep=";")

source_1_data = pd.read_csv("../data/trial1/symptoms_diseases_mapping_source_1.csv", sep=';', encoding="ISO-8859-1")
source_2_data = pd.read_csv("../data/trial1/symptoms_diseases_mapping_source_2.csv", sep=';', encoding="ISO-8859-1")
resultData = pd.concat([source_1_data, source_2_data])
resultData.drop_duplicates(keep='first', inplace=True)
resultData['symptom_name'] = resultData['symptom_name'].str.lower()
resultData['disease_common_name'] = resultData['disease_common_name'].str.lower()
resultData.to_csv("../data/trial1/symptoms_diseases_mapping_merged.csv", index=False, sep=";")

data = pd.read_csv("../data/trial1/symptoms_diseases_mapping_merged.csv", sep=";", encoding="ISO-8859-1")
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
df_pivoted.to_csv("../data/trial1/symptoms_disease_pivoted.csv", index=False, sep=";")

data = pd.read_csv("../data/trial1/symptoms_disease_pivoted.csv", encoding="ISO-8859-1", sep=";")
columns = list(data.columns.values)
resultData = data.copy()
for index, row in data.iterrows():
    disease_name = row[-1]
    indices = [i for i in range(0, len(columns) -1) if row[i] == 1.0]
    for i in range(NO_OF_DUPLICATES):
        df_try = data.loc[data['disease_common_name'] == disease_name]
        df_try = df_try.copy()
        if len(indices) > 1:
            df_try[data.columns[indices[random.randint(0, len(indices)-1)]]] = 0
        resultData = resultData.append(df_try, ignore_index=True)
resultData.to_csv("../data/trial1/disease_prediction_input.csv", index=False, sep=";")

with open("../data/trial1/disease_prediction_input.csv") as inp, open("../data/trial1/apriori_input_partial.csv", 'w') as o1:
    next(inp)
    for line in inp:
        symptoms = line.strip('\n').split(';')
        disease = symptoms.pop()
        present_symptoms = [columns[indx] for indx, val in enumerate(symptoms) if val == "1.0"]
        present_symptoms = ";".join(present_symptoms)
        o1.write("{}\n".format(present_symptoms))

dataset = pd.DataFrame()
with open("../data/trial1/apriori_input_partial.csv", 'r', errors = 'ignore') as f:
    for line in f:
        dataset = pd.concat( [dataset, pd.DataFrame([tuple(line.strip().split(';'))])], ignore_index=True )
        dataset = dataset.drop_duplicates()
print("data read")
with open("../data/trial1/apriori_input.csv", 'w', errors = 'ignore') as f:
    for i in range(0, len(dataset.index)):
        f.write("\n"+(";".join([str(dataset.values[i,j]) for j in range(0, len(dataset.columns)) if str(dataset.values[i,j]) != 'nan'])))
print("converted to transactions")