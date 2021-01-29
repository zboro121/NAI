from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import pandas as pd
from LAB6.Classification import Classification


class FashionMNISTExample:
    """ Runs Fashion MNIST Example.
    More info: https://github.com/zalandoresearch/fashion-mnist"""

    def __init__(self, algorithm):
        self.dataset = pd.read_csv('data/Fashion-MNIST/train.csv')
        self.algorithm = Classification(algorithm)

    def run(self):
        """
        Runs example.
        """
        X_train, X_test, y_train, y_test = self.__prepare_data(['Id', 'Category'], 'Category')
        self.algorithm.train_model(X_train, X_test, y_train, y_test)

    def __prepare_data(self, drop_columns, output_column):
        """
        Splits the data into train and test batches.
        :param drop_columns: columns to drop
        :param output_column: output column
        :returns: Data split into X_train, X_test, y_train, y_test
        """
        X = self.dataset.drop(drop_columns, axis='columns')
        y = self.dataset[output_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        return X_train, X_test, y_train, y_test
