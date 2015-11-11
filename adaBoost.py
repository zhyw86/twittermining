from sklearn.ensemble import AdaBoostClassifier
from numpy import genfromtxt

train_data = genfromtxt("./data.csv", delimiter=',')

boost = AdaBoostClassifier()

boost = boost.fit(train_data[0:100], train_data[0:100, 59])

output = boost.predict(train_data)

i = 0
for x in output:
    print i, ":", x
    i = i + 1
