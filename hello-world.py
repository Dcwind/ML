import sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

# in labels 0 for apples and 1 for oranges
classifier = tree.DecisionTreeClassif()
classifier = classifier.fit(features, labels)

