import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

dataset = pd.read_csv('indian-dataset.txt', sep=",", header=None)
dataset.columns = ["No times pregnant", "Plasma glucose",
                   "blood pressure", "skinfold thickness", "2-Hour serum insulin",
                   "BMI", "Diabetes pedigree function", "Age", "Class"]
# print(dataset.head())
# print(dataset.describe())
# df = pd.DataFrame(dataset, columns=dataset.columns)
# print(df.head())

# df0 = dataset[dataset.Class == 0]
# print(df0)
# df1 = dataset[dataset.Class == 1]
# print(df1)
# plt.scatter(df0['No times pregnant'], df0['BMI'], color='blue', marker='*')
# plt.scatter(df1['No times pregnant'], df1['BMI'], color='green', marker='+')
# plt.show()

X = dataset.drop('Class', axis='columns')
# print(X)
Y = dataset.Class
# print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = SVC()
model_fit = model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))




