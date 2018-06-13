import pickle

rules={}
with open('../resources/state/rules.pkl', 'rb') as input_file:
    rules = pickle.load(input_file)


def filter_out_suggested_symptoms(vals, symptoms=[]):
    return [ele for ele in vals if ele[0] not in symptoms]


def predict_next(p, pos, neg):
    next_sugg = None
    pos_set = set(pos)
    max_intersection = 0
    for sugg in p:  # ( s1, s2, s3 )           pos : [s2, s3]
        intersec = set(sugg).intersection(pos_set)
        intersec_len = len(intersec)
        if intersec_len > max_intersection:
            max_intersection = intersec_len
            next_sugg = sugg
    if next_sugg:
        # print(max_intersection, intersec_len, next_sugg)
        next_pred = p[next_sugg]
        return next_pred[0][0]  # can check the confidence as well here.
    else:
        return None


def predict_next_symptoms(positive=[], negative=[]):
    possibilities = {}
    for k in rules.keys():
        for symptom in positive:
            if symptom in k and k not in possibilities:
                filtered_vals = filter_out_suggested_symptoms(rules[k], positive + negative)
                if filtered_vals:
                    possibilities[k] = filtered_vals

    # filter out right side for both negative and positive items.
    possibilities_dup = possibilities.copy();
    for k, v in possibilities_dup.items():
        filtered_right_side = [s for s in v if s[0] != symptom]
        if filtered_right_side:
            possibilities[k] = filtered_right_side
        else:
            del possibilities[k]

    possible_symptoms = list([]);
    for k, v in possibilities.items():
        for s in v:
            possible_symptoms.append(s)

    print("Positive symptoms: \n", positive)
    print("Negative symptoms: \n", negative)
    print("Next possible Symptoms: \n", possible_symptoms)
    return (possible_symptoms, possibilities)


def predict_next_symptom(positive=[], negative=[]):
    answer = predict_next_symptoms(positive, negative);
    next_symptom = predict_next(answer[1], positive, negative)
    return next_symptom
