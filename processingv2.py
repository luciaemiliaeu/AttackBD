import pandas as pd 
import numpy as np 
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

# import dataset
data = pd.read_csv('data_attackv5.csv', sep =',')
X = data.drop('label', axis=1)
y = data['label']

# modelos 
names = ["Nearest Neighbors", "Linear SVM", "RBF SVM",
		 "Decision Tree", "Random Forest","Naive Bayes", "Neural Net"]

classifiers = [
	KNeighborsClassifier(3),
	SVC(kernel="linear", C=0.025),
	SVC(gamma=2, C=1),
	DecisionTreeClassifier(max_depth=5),
	RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
	GaussianNB(),
	MLPClassifier(alpha=1, max_iter=1000),
	]

# Testes 
results = pd.DataFrame(columns =['Pct_treino', 'Algoritmo', 'Acuracia'])
pct = 0.1
while pct< 0.99:
	print('training with ', str(pct) , "%...")
	for ext in range(10):
		X_test = X.sample(frac=pct)
		y_test = y.loc[X_test.index].values

		X_train = X.drop(X_test.index)
		y_train = y.loc[X_train.index].values

		X_test = X_test.values
		X_train = X_train.values

		for name, clf in zip(names, classifiers):
			clf.fit(X_train, y_train)
			score = clf.score(X_test, y_test)
			results.loc[results.shape[0],:] = [pct, name, score]
	pct += 0.1

results.to_csv('results.csv',index=False, sep =',')

