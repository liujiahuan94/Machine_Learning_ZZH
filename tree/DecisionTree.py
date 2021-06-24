import numpy as np
from sklearn.datasets import load_iris


class Data():
    def __init__(self):
        self.data = load_iris()


class Node:
    def __init__(self, left, right, rule):
        self.left = left
        self.right = right
        self.feature = rule[0]
        self.threshold = rule[1]


class Leaf:
    def __init__(self, value):
        """
        'value' is an array of class probabilities if classfier is True, else
        the mean of the region
        """
        self.value = value


class DecisionTree:
    
        

iris_data = Data().data
print(iris_data['data'][0])




