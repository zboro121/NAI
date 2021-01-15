import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

dataset = pd.read_csv('adult.data.txt', sep=",", header=None)
dataset.columns = ["age", "workclass", "fnlwgt", "education", "education-num",
                   "marital-status", "occupation", "relationship", "race",
                   "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "earnings"]

# print(dataset.dtypes)
# print(dataset)
dataset['earnings'].replace(['<=50K', '>50K'], [0, 1], inplace=True, regex=True)
# print(dataset)
dummies = pd.get_dummies(dataset).head(3000)
# print(dummies.head())
# print(dummies.dtypes)

X = dummies.drop('earnings', axis='columns')
# print(X)
Y = dummies['earnings']
# print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
model = SVC()
model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))