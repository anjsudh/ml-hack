import timeit

import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB

with open("../data/models/accuracies.csv", 'w') as output_file:
    data = pd.read_csv("../data/trial2/disease_prediction_input.csv", header=0, sep=';')
    headers = list(data.columns.values)
    x = data.iloc[:, 0:-1].values
    y = data.iloc[:, -1].values
    from sklearn.cross_validation import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    output_file.write(("model,correct predictions,total predictions,accuracy,execution time\n"))

    start_time = timeit.default_timer()
    classifier = MultinomialNB()
    classifier = classifier.fit(x, y)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % ("multinomial_naive_bayes", sum_first_diagonal, sum_all, sum_first_diagonal/sum_all, end_time-start_time)))
    np.savetxt('../data/models/confusion_matrix_mnb.txt',cm,fmt='%.2f')

    start_time = timeit.default_timer()
    classifier = BernoulliNB()
    classifier = classifier.fit(x, y)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % (
    "bernouli_naive_bayes", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time - start_time)))
    np.savetxt('../data/models/confusion_matrix_bnb.txt', cm, fmt='%.2f')

    start_time = timeit.default_timer()
    classifier = GaussianNB()
    classifier = classifier.fit(x, y)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % (
    "gaussian_naive_bayes", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time - start_time)))
    np.savetxt('../data/models/confusion_matrix_gnb.txt', cm, fmt='%.2f')

    start_time = timeit.default_timer()
    from sklearn.svm import SVC
    classifier = SVC(kernel = 'linear', C=0.65)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % ("svm", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time-start_time)))
    np.savetxt('../data/models/confusion_matrix_svm.txt',cm,fmt='%.2f')

    start_time = timeit.default_timer()
    from sklearn.svm import LinearSVC

    classifier = LinearSVC( C=0.65)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % (
    "linear_svm", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time - start_time)))
    np.savetxt('../data/models/confusion_matrix_lsvm.txt', cm, fmt='%.2f')

    start_time = timeit.default_timer()
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % ("random_forest", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time-start_time)))
    np.savetxt('../data/models/confusion_matrix_rf.txt',cm,fmt='%.2f')

    start_time = timeit.default_timer()
    from sklearn.ensemble import VotingClassifier

    classifier = VotingClassifier(estimators=[('mnb', MultinomialNB()), ('bnb', BernoulliNB()), ('gnb', GaussianNB())])
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % (
    "voting", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time - start_time)))
    np.savetxt('../data/models/confusion_matrix_voting.txt', cm, fmt='%.2f')

    start_time = timeit.default_timer()
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    end_time = timeit.default_timer()
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    sum_first_diagonal = sum(cm[i][i] for i in range(len(cm)))
    sum_all = sum(np.sum(cm, axis=0))
    output_file.write(("%s,%s,%s,%0.2f,%0.2f\n" % ("decision_tree", sum_first_diagonal, sum_all, sum_first_diagonal / sum_all, end_time-start_time)))
    np.savetxt('../data/models/confusion_matrix_dt.txt',cm,fmt='%.2f')
