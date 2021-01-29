# Authors: Paweł Zborowski, Jakub Wirkus
# Problem: Classification using MLP
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

from LAB6.Examples.FashionMNISTExample import FashionMNISTExample
from LAB6.Examples.LetterRecognitionExample import LetterRecognitionExample
from LAB6.Examples.PimaIndiansExample import PimaIndiansExample
from LAB6.Examples.Cifar10Example import Cifar10Example

if __name__ == '__main__':
    print("------------------------Pima Indians example------------------------")
    print("------------------------SVC------------------------")
    primaIndiansSVC = PimaIndiansExample(SVC())
    primaIndiansSVC.run()
    print("------------------------MLP------------------------")
    print("--------SMALL LAYER SIZE--------")
    primaIndiansMLP_small = PimaIndiansExample(
        MLPClassifier(max_iter=5000, warm_start=True, verbose=False, random_state=1,
                      hidden_layer_sizes=(10,)))
    primaIndiansMLP_small.run()
    print("---------BIG LAYER SIZE---------")
    primaIndiansMLP_big = PimaIndiansExample(
        MLPClassifier(max_iter=5000, warm_start=True, verbose=False, random_state=1,
                      hidden_layer_sizes=(100, 100)))
    primaIndiansMLP_big.run()

    print("------------------------Fashion MNIST Example-------------------------")
    print("------------------------MLP------------------------")
    print("--------SMALL LAYER SIZE--------")
    fMnistMLP_small = FashionMNISTExample(MLPClassifier(max_iter=500, warm_start=True, verbose=False, random_state=1,
                                                        hidden_layer_sizes=(10,)))
    fMnistMLP_small.run()
    print("---------BIG LAYER SIZE---------")
    fMnistMLP_big = FashionMNISTExample(MLPClassifier(max_iter=500, warm_start=True, verbose=False, random_state=1,
                                                      hidden_layer_sizes=(100, 100)))
    fMnistMLP_big.run()

    print("----------------------------CIFAR10 Example------------------------------")
    print("------------------------MLP------------------------")
    print("--------SMALL LAYER SIZE--------")
    cifar10MLP_small = Cifar10Example(MLPClassifier(max_iter=2000, warm_start=True, verbose=False, random_state=1,
                                                    hidden_layer_sizes=(20,)))
    cifar10MLP_small.run()
    print("---------BIG LAYER SIZE---------")
    cifar10MLP_big = Cifar10Example(MLPClassifier(max_iter=2000, warm_start=True, verbose=False, random_state=1,
                                                  hidden_layer_sizes=(100, 100)))
    cifar10MLP_big.run()

    print("-----------------------Letter Recognition Example--------------------------")
    print("------------------------MLP------------------------")
    print("--------SMALL LAYER SIZE--------")
    letterRecExample_small = LetterRecognitionExample(
        MLPClassifier(max_iter=5000, warm_start=True, verbose=False, random_state=1,
                      hidden_layer_sizes=(17,)))
    letterRecExample_small.run()
    print("---------BIG LAYER SIZE---------")
    letterRecExample_big = LetterRecognitionExample(
        MLPClassifier(max_iter=5000, warm_start=True, verbose=False, random_state=1,
                      hidden_layer_sizes=(100, 100)))
    letterRecExample_big.run()
