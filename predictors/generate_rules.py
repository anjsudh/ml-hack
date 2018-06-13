
import pandas as pd

def generate_rules_obj(file):
    rule_dict = {}
    rules_data = pd.read_csv(file, encoding="ISO-8859-1", sep='|', header=None)
    rules_data = rules_data.drop_duplicates()

    for row in rules_data.iterrows():
        val = (row[1][1], row[1][2])
        symptom_group = tuple(sorted(row[1][0].split(';')))
        if symptom_group in rule_dict:
            rule_dict[symptom_group].append(val)
        else:
            if len(row[1][1].split(';')) <= 1:
                rule_dict[symptom_group] = [val]
    rules = dict(rule_dict)

    import pickle;
    with open('../resources/state/rules.pkl', 'wb') as output_file:
        pickle.dump(rules, output_file)
