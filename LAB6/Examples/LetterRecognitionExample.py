import pandas as pd
from sklearn.model_selection import train_test_split

from LAB6.Classification import Classification


class LetterRecognitionExample:
    """ Runs Lette rRecognition Example.
    Dataset source: https://archive.ics.uci.edu/ml/datasets/letter+recognition?fbclid=IwAR0VhB2EGYaFlHO2xaUuDbEvhBgmBGcvdoFGOKUBxk3nVa8926zsL3DF-Nk """

    def __init__(self, algorithm):
        self.dataset = pd.read_csv('data/letter-recognition.data')
        self.algorithm = Classification(algorithm)

    def run(self):
        """
        Runs example.
        """
        X_train, X_test, y_train, y_test = self.__prepare_data('Letter', 'Letter')
        self.algorithm.train_model(X_train, X_test, y_train, y_test)

    def __prepare_data(self, drop_columns, output_column):
        """
        Splits the data into train and test batches.
        :param drop_columns: columns to drop
        :param output_column: output column
        :returns: Data split into X_train, X_test, y_train, y_test
        """
        columns = ["Letter", "x-box horizontal pos",
                   "y-box vertical pos", "width", "height",
                   "onpix total #", "x-bar mean x of on pixels", "y-bar mean y of on pixels", "x2bar mean x var",
                   "y2bar mean y var", "xybar mean x y correl", "x2ybr mean of x * x * y", "xy2br mean of x * y * y",
                   "x-ege mean edge count left to right", "xegvy correlation of x-ege with y",
                   "y-ege mean edge count bottom to top", "yegvx correlation of y-ege with x"]
        self.dataset.columns = columns
        X = self.dataset.drop(drop_columns, axis='columns')
        y = self.dataset[output_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        return X_train, X_test, y_train, y_test
