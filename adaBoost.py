from sklearn.ensemble import AdaBoostClassifier
from numpy import genfromtxt

train_data = genfromtxt("./data.csv", delimiter=',')

boost = AdaBoostClassifier()

boost = boost.fit(train_data[0:10000], train_data[0:10000, 59])

output = boost.predict(train_data)


for x in output:
    status = 'unpopular'
    if x > 1400:
        status = 'popular'

    print "%lf,%s" % (x, status)
