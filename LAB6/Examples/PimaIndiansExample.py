import pandas as pd
from sklearn.model_selection import train_test_split

from LAB6.Classification import Classification


class PimaIndiansExample:
    """ Runs Pima Indians Example.
    More info: https://machinelearningmastery.com/standard-machine-learning-datasets/
    Dataset source: https://machinelearningmastery.com/standard-machine-learning-datasets/"""

    def __init__(self, algorithm):
        self.dataset = pd.read_csv('data/indian-dataset.txt')
        self.algorithm = Classification(algorithm)

    def run(self):
        """
        Runs example.
        """
        X_train, X_test, y_train, y_test = self.__prepare_data('Class', 'Class')
        self.algorithm.train_model(X_train, X_test, y_train, y_test)

    def __prepare_data(self, drop_columns, output_column):
        """
        Splits the data into train and test batches.
        :param drop_columns: columns to drop
        :param output_column: output column
        :returns: Data split into X_train, X_test, y_train, y_test
        """
        columns = ["No times pregnant", "Plasma glucose",
                   "blood pressure", "skinfold thickness", "2-Hour serum insulin",
                   "BMI", "Diabetes pedigree function", "Age", "Class"]
        self.dataset.columns = columns
        X = self.dataset.drop(drop_columns, axis='columns')
        y = self.dataset[output_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        return X_train, X_test, y_train, y_test
