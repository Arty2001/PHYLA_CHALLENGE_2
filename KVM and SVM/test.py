



import numpy as np
import TestTrain
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


dataset = pd.read_csv('challenge_1_gut_microbiome_data.csv',  sep=",", header=None, low_memory= False)
print(dataset)



x = dataset.iloc[ 1 : , 1 : -1].values
y = dataset.iloc[1 :, -1].values




scaler = StandardScaler()
x_scale = scaler.fit_transform(x)
x_scale



xTrain , xTest , yTrain , yTest = train_test_split(x_scale , y , test_size = 0.20 , random_state = 6)
# xTrain , yTrain = TestTrain.testTrain(x_scale, y)






classifier = KNeighborsClassifier(n_neighbors = 20)
classifier.fit(xTrain, yTrain)


yPred = classifier.predict(xTest)



print(classification_report(yTest, yPred))
print(confusion_matrix(yTest, yPred))





# accuracies = []
# for i in range(1,42):
#     xTrain , xTest , yTrain , yTest = train_test_split(x_scale , y , test_size = 0.20, random_state=i )
#     classifier = KNeighborsClassifier(n_neighbors = 20)
#     classifier.fit(xTrain, yTrain)
#     yPred = classifier.predict(xTest)
#     st = classification_report(yTest, yPred).split()
#     for j in range(len(st)):
#         if st[j] == 'accuracy':
#             accuracies.append(st[j + 1])


classifierSVM = SVC(kernel = "rbf", random_state = 0)
classifierSVM.fit(xTrain, yTrain)
yPredSVM = classifierSVM.predict(xTest)


print(classification_report(yTest, yPredSVM))
print(confusion_matrix(yTest, yPredSVM))




