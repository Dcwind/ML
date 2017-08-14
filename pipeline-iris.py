# import dataset
from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

# split train and test dataset
from sklearn.cross_validation import train_test_split