from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score


class Classification:
    """ Creates a model of given dataset """

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def train_model(self, X_train, X_test, y_train, y_test):
        """
        Calculates model.
        :param X_train: train data - input
        :param X_test: test data - input
        :param y_train: train data - input
        :param y_test: test data - output
        :returns: model
        """
        model = self.algorithm
        model.fit(X_train, y_train)
        self.__print_report(model, X_test, y_test)
        return model

    @staticmethod
    def __print_report(model, X_test, y_test):
        """
        Prints classification report.
        :param X_test: model to test
        :param X_test: test data - input
        :param y_test: test data - output
        """
        scores = cross_val_score(model, X_test, y_test, cv=10)
        print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
        pred = model.predict(X_test)
        print(classification_report(y_test, pred))






