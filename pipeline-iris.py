from scipy.spatial import distance
import random

def euc(a, b):
    return distance.euclidean(a,b)

class ScrappyKKN():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        for row in x_test:
            label = random.choice(self.y_train)
            predictions.append(label)

        return predictions

# import dataset
from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

# split train and test dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

# import classifier
from sklearn import tree
# my_classifier =  tree.DecisionTreeClassifier()

# from sklearn.neighbors import KNeighborsClassifier
my_classifier =  ScrappyKKN()

# train classifier
my_classifier.fit(x_train, y_train)

predictions =  my_classifier.predict(x_test)

# test accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))