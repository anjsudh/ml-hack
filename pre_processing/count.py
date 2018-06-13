import pandas as pd

data = pd.read_csv("../data/trial2/symptoms.csv", encoding="ISO-8859-1")
cols = data.columns.tolist()
cols = [cols[0]]
data = data[cols]
data = data.drop_duplicates()
print (data)
print(len(data.index))
data.to_csv("../data/trial2/diseases.csv")