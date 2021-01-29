from LAB6.Classification import Classification
from keras.datasets import cifar10


class Cifar10Example:
    """ Runs CIFAR10 example. Uses keras (tensorflow) to fetch dataset"""

    def __init__(self, algorithm):
        self.dataset = cifar10.load_data()
        self.algorithm = Classification(algorithm)

    def run(self):
        """
        Runs example.
        """
        X_train, X_test, y_train, y_test = self.__prepare_data()
        self.algorithm.train_model(X_train, X_test, y_train, y_test)

    def __prepare_data(self):
        """
        Prepares the data. Based on
        'athena.ecs.csus.edu/~hoangkh/Image Classification with Fashion-MNIST and CIFAR-10.html'.
        :returns: Data split into X_train, X_test, y_train, y_test
        """
        (X_train, y_train), (X_test, y_test) = self.dataset

        X_train = X_train.astype('float32')
        X_test = X_test.astype('float32')
        X_train /= 255
        X_test /= 255

        x_train_flat = X_train.reshape(X_train.shape[0], X_train.shape[1] * X_train.shape[2] * X_train.shape[3])
        x_test_flat = X_test.reshape(X_test.shape[0], X_test.shape[1] * X_test.shape[2] * X_test.shape[3])

        y_train = y_train.reshape(y_train.shape[0], )
        y_test = y_test.reshape(y_test.shape[0], )
        return x_train_flat, x_test_flat, y_train, y_test
