import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_idx = [0, 50, 100]

#display dataset
for i  in range(len(iris.target)):
    print("Example %d:  label %s, features %s" % (i, iris.data[i], iris.target[i]))

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# train classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

# test
print(test_target)
print(clf.predict(test_data))

